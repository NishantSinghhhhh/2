// algolia-search.js — InstantSearch.js v4
(function () {
  const appId    = document.getElementById('algolia-search').dataset.appId;
  const apiKey   = document.getElementById('algolia-search').dataset.apiKey;
  const indexName = document.getElementById('algolia-search').dataset.indexName;

  const searchClient = algoliasearch(appId, apiKey);

  const search = instantsearch({
    indexName,
    searchClient,
    searchFunction(helper) {
      const query = helper.state.query;
      const resultsEl = document.getElementById('search-results');
      if (!query || query.trim() === '') {
        resultsEl.style.display = 'none';
        return;
      }
      helper.search();
      resultsEl.style.display = 'block';
    }
  });

  search.addWidgets([
    instantsearch.widgets.searchBox({
      container: '#search-input',
      placeholder: 'Search (' + (/Mac|iPhone|iPad/.test(navigator.platform) ? '⌘K' : 'Ctrl+K') + ')',
      autofocus: false,
      showReset: true,
      showLoadingIndicator: true,
    }),

    instantsearch.widgets.hits({
      container: '#search-results',
      templates: {
        item(hit, { html, components }) {
          const url = hit.url + (hit.anchor ? '#' + hit.anchor : '');
          const breadcrumbs = (hit._highlightResult.headings || [])
            .map(h => `<span class="result-breadcrumb">${h.value}</span>`)
            .join(' › ');

          return html`
            <div class="result-item">
              <h4>
                <a class="result-link" href="${url}">
                  ${components.Highlight({ hit, attribute: 'title' })}
                </a>
              </h4>
              ${breadcrumbs
                ? html`<div class="result-breadcrumbs">${breadcrumbs}</div>`
                : ''}
              <div class="result-snippet">
                ${components.Snippet({ hit, attribute: 'html' })}
              </div>
            </div>
          `;
        },
        empty(results, { html }) {
          return html`<div class="result-empty">No results for <strong>${results.query}</strong></div>`;
        }
      }
    })
  ]);

  search.start();

  // ── Keyboard shortcuts ──────────────────────────────────────
  document.addEventListener('keydown', function (e) {
    const isMac = /Mac|iPhone|iPad|iPod/.test(navigator.platform);

    // Cmd/Ctrl+K → focus search
    if ((isMac ? e.metaKey : e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      const input = document.querySelector('#search-input input');
      if (input) { input.focus(); input.select(); }
    }

    // Escape → close results
    if (e.key === 'Escape') {
      document.getElementById('search-results').style.display = 'none';
      const input = document.querySelector('#search-input input');
      if (input) input.blur();
    }
  });

  // ── Click outside → close results ───────────────────────────
  document.addEventListener('mouseup', function (e) {
    const results = document.getElementById('search-results');
    const inputEl = document.getElementById('search-input');
    if (!results.contains(e.target) && !inputEl.contains(e.target)) {
      results.style.display = 'none';
    }
  });

  document.addEventListener('mouseup', function (e) {
    const inputEl = document.getElementById('search-input');
    if (inputEl.contains(e.target)) {
      const q = document.querySelector('#search-input input');
      if (q && q.value.trim() !== '') {
        document.getElementById('search-results').style.display = 'block';
      }
    }
  });
})();