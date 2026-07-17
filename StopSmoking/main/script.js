const button = document.getElementById('countButton');
const removeButton = document.getElementById('removeButton');
const counterValue = document.getElementById('counterValue');
const moneyValue = document.getElementById('moneyValue');
const resetButton = document.getElementById('resetButton');
const historyList = document.getElementById('historyList');
const themeToggle = document.getElementById('themeToggle');
const themeStorageKey = 'smoke-tracker-theme';
const storageKey = 'smoke-tracker-data';
const packCost = 500;
const perCigaretteCost = 25;
const maxHistoryDays = 7;
const retentionDays = 100;

function getTodayKey() {
  return new Date().toISOString().split('T')[0];
}

function pruneOldDays(data) {
  if (!data || !data.days) return;
  const dates = Object.keys(data.days).sort((a, b) => b.localeCompare(a));
  if (dates.length <= retentionDays) return;
  const toKeep = new Set(dates.slice(0, retentionDays));
  Object.keys(data.days).forEach((d) => {
    if (!toKeep.has(d)) delete data.days[d];
  });
}

function createDayData(date) {
  return { date, count: 0, moneyLeft: packCost };
}

function createDefaultData() {
  const today = getTodayKey();
  return {
    currentDate: today,
    days: {
      [today]: createDayData(today)
    }
  };
}

function migrateOldData(parsed) {
  if (parsed && typeof parsed === 'object' && parsed.date) {
    const date = String(parsed.date);
    const day = createDayData(date);
    pruneOldDays(parsed);
    day.count = Number(parsed.count) || 0;
    day.moneyLeft = Number(parsed.moneyLeft ?? packCost) || packCost;
    const today = getTodayKey();
    return {
      currentDate: today,
      days: {
        [date]: day,
        [today]: date === today ? day : createDayData(today)
      }
    };
  }

  return createDefaultData();
}

function loadData() {
  const raw = localStorage.getItem(storageKey);
  if (!raw) {
    return createDefaultData();
  }

  try {
    const parsed = JSON.parse(raw);
    if (!parsed || typeof parsed !== 'object' || typeof parsed.currentDate !== 'string' || typeof parsed.days !== 'object') {
      return migrateOldData(parsed);
    }

    const today = getTodayKey();
    if (!parsed.days[today]) {
      parsed.days[today] = createDayData(today);
    }

    parsed.currentDate = today;
    return parsed;
  } catch {
    return createDefaultData();
  }
}

function saveData(data) {
  localStorage.setItem(storageKey, JSON.stringify(data));
}

function getCurrentDay(data) {
  if (!data.days[data.currentDate]) {
    data.days[data.currentDate] = createDayData(data.currentDate);
  }
  return data.days[data.currentDate];
}

function renderHistory(data) {
  if (!historyList) {
    return;
  }

  const allDays = Object.values(data.days).sort((a, b) => b.date.localeCompare(a.date));
  const daysToShow = allDays.slice(0, maxHistoryDays);

  if (daysToShow.length === 0) {
    historyList.innerHTML = '<li>No history yet.</li>';
    return;
  }

  historyList.innerHTML = '';
  daysToShow.forEach((day) => {
    const listItem = document.createElement('li');
    listItem.textContent = `${day.date}: ${day.count} cigarettes — ¥${day.moneyLeft} left`;
    if (day.date === data.currentDate) {
      listItem.classList.add('today');
      listItem.textContent = `${day.date} (today): ${day.count} cigarettes — ¥${day.moneyLeft} left`;
    }
    historyList.appendChild(listItem);
  });
}

function render() {
  const data = loadData();
  const today = getCurrentDay(data);

  counterValue.textContent = today.count;
  moneyValue.textContent = `${today.moneyLeft}`;
  renderHistory(data);
  saveData(data);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  if (themeToggle) {
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
    themeToggle.setAttribute('aria-pressed', theme === 'dark');
  }
}

function loadTheme() {
  let t = localStorage.getItem(themeStorageKey);
  if (!t) {
    t = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  applyTheme(t);
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    localStorage.setItem(themeStorageKey, next);
  });
}

button.addEventListener('click', () => {
  const data = loadData();
  const today = getCurrentDay(data);
  today.count += 1;
  today.moneyLeft = Math.max(0, today.moneyLeft - perCigaretteCost);
  saveData(data);
  render();
});

removeButton.addEventListener('click', () => {
  const data = loadData();
  const today = getCurrentDay(data);
  if (today.count <= 0) {
    return;
  }
  today.count -= 1;
  today.moneyLeft = Math.min(packCost, today.moneyLeft + perCigaretteCost);
  saveData(data);
  render();
});

resetButton.addEventListener('click', () => {
  const data = loadData();
  data.days[data.currentDate] = createDayData(data.currentDate);
  saveData(data);
  render();
});

loadTheme();
render();
