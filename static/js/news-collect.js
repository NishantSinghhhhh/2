document.addEventListener("DOMContentLoaded", function () {
  const newsContainer = document.getElementById("news-container");
  const loadingText  = document.getElementById("loading-news");

  /* ── icon picked by tag/category keyword ─────────────────── */
  function getIcon(title = "") {
    const text = title.toLowerCase();
    if (text.includes("release") || text.includes("update") || text.includes("version"))
      return "fas fa-rocket";
    if (text.includes("workshop") || text.includes("event") || text.includes("conference"))
      return "fas fa-calendar-alt";
    if (text.includes("tutorial") || text.includes("doc") || text.includes("guide"))
      return "fas fa-book-open";
    if (text.includes("paper") || text.includes("publication") || text.includes("research"))
      return "fas fa-file-alt";
    return "fas fa-newspaper";
  }

  /* ── category label ───────────────────────────────────────── */
  function getCategory(title = "") {
    const text = title.toLowerCase();
    if (text.includes("release") || text.includes("update") || text.includes("version"))
      return "Update";
    if (text.includes("workshop") || text.includes("event") || text.includes("conference"))
      return "Event";
    if (text.includes("tutorial") || text.includes("doc") || text.includes("guide"))
      return "Documentation";
    if (text.includes("paper") || text.includes("publication"))
      return "Publication";
    return "News";
  }

  /* ── build one card ───────────────────────────────────────── */
  function buildCard({ url, title, desc, date }) {
    const icon     = getIcon(title);
    const category = getCategory(title);
    const dateStr  = date
      ? new Date(date).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" })
      : "";

    const card = document.createElement("div");
    card.className = "news-card";
    card.innerHTML = `
      <div class="news-card-thumb">
        <i class="${icon}"></i>
      </div>
      <div class="news-card-body">
        <div class="news-card-tag">
          ${category}${dateStr ? ` <span class="news-card-date">· ${dateStr}</span>` : ""}
        </div>
        <h4 class="news-card-title">${title}</h4>
        ${desc ? `<p class="news-card-desc">${desc}</p>` : ""}
        <a href="${url}"
           target="_blank"
           rel="noopener noreferrer"
           class="news-card-link no-external-marker">
          Read more <i class="fas fa-arrow-right"></i>
        </a>
      </div>
    `;
    return card;
  }

  /* ── hardcoded fallback data ──────────────────────────────── */
  function getStaticNews() {
    return [
      {
        url:   "https://precice.discourse.group/t/precice-at-gsoc/",
        title: "We need help from experienced preCICE users on GitHub - preCICE at GSoC",
        desc:  "We need the help of experienced community members in reviewing an unprecedented amount of community contributions on GitHub. If you always wanted to actively contribute, but didn't know where to start — this is your chance.",
        date:  "2026-03-02",
      },
      {
        url:   "https://precice.discourse.group/t/precice-at-eccomas-wccm-2026/",
        title: "preCICE at ECCOMAS WCCM 2026 (Munich, Germany)",
        desc:  "Besides the preCICE Workshops, we regularly organize preCICE sessions in larger conferences. The WCCM 2026 conference will take place in Munich, Germany. Join us for talks and discussions on the latest in multi-physics coupling.",
        date:  "2025-12-01",
      },
      {
        url:   "https://precice.discourse.group/t/new-preprint-waveform-iteration/",
        title: "New preprint on waveform iteration",
        desc:  "We just uploaded a new preprint on arXiv: A waveform iteration implementation for black-box multi-rate higher-order coupling — a compact summary of the dissertation of Benjamin Rodenberg.",
        date:  "2025-11-12",
      },
    ];
  }

  /* ── render ───────────────────────────────────────────────── */
  function render() {
    // Directly grab the static news
    const topics = getStaticNews();

    // Hide the loading text if it exists
    if (loadingText) loadingText.style.display = "none";
    
    // Build and append each card
    topics.forEach(t => newsContainer.appendChild(buildCard(t)));
  }

  // Execute render
  render();
});