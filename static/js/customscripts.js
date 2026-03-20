$(document).ready(function () {

  // ── Tooltips ───────────────────────────────────────────────
  $('[data-toggle="tooltip"]').tooltip({
    placement: 'top'
  });

  // ── AnchorJS ──────────────────────────────────────────────
  anchors.add('main h2:not(.no-anchor),main h3:not(.no-anchor),main h4:not(.no-anchor),main h5:not(.no-anchor)');

  // ── Sidebar: bubble active class up to parent <li> ────────
  // Only runs if Hugo already set class="active" on a child <li>
  // (i.e. the current page matched a folderitem URL in sidebar.html)
  $("#mysidebar li.active").parents("li").addClass("active");

  // ── Top-level: collapse all, then open only the active one ─
  $("#mysidebar > li > ul").hide();
  $("#mysidebar > li.active > ul").show();
  $("#mysidebar > li.active > a").addClass("expanded");

  // ── Top-level: toggle on click ────────────────────────────
  $("#mysidebar > li > a").on("click", function (e) {
    var $li = $(this).parent();
    var $ul = $li.children("ul");

    // No submenu — let the link navigate normally
    if ($ul.length === 0) return;

    e.preventDefault();

    var isOpen = $ul.is(":visible");

    // Close every top-level section first
    $("#mysidebar > li > ul").slideUp(200);
    $("#mysidebar > li > a").removeClass("expanded");

    // If it was closed, open it now
    if (!isOpen) {
      $ul.slideDown(200);
      $(this).addClass("expanded");
    }
  });

  // ── Subfolder: collapse all, then open only the active one ─
  $("#mysidebar > li > ul > li.subfolders > ul").hide();
  $("#mysidebar > li > ul > li.subfolders.active > ul").show();
  $("#mysidebar > li > ul > li.subfolders.active > a").addClass("expanded");

  // ── Subfolder: toggle on click ────────────────────────────
  $("#mysidebar > li > ul > li.subfolders > a").on("click", function (e) {
    var $li = $(this).parent();
    var $ul = $li.children("ul");

    if ($ul.length === 0) return;

    e.preventDefault();

    var isOpen = $ul.is(":visible");

    // Close all sibling subfolders within the same parent ul
    var $parentUl = $(this).closest("ul");
    $parentUl.find("li.subfolders > ul").slideUp(200);
    $parentUl.find("li.subfolders > a").removeClass("expanded");

    if (!isOpen) {
      $ul.slideDown(200);
      $(this).addClass("expanded");
    }
  });

});

// ── Nav tabs: persist active tab across page loads ───────────
$(function () {
  var json, tabsState;

  $('a[data-toggle="pill"], a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    tabsState = localStorage.getItem("tabs-state");
    json = JSON.parse(tabsState || "{}");
    var parentId = $(e.target).parents("ul.nav.nav-pills, ul.nav.nav-tabs").attr("id");
    var href = $(e.target).attr('href');
    json[parentId] = href;
    localStorage.setItem("tabs-state", JSON.stringify(json));
  });

  tabsState = localStorage.getItem("tabs-state");
  json = JSON.parse(tabsState || "{}");

  $.each(json, function (containerId, href) {
    $("#" + containerId + " a[href=" + href + "]").tab('show');
  });

  $("ul.nav.nav-pills, ul.nav.nav-tabs").each(function () {
    var $this = $(this);
    if (!json[$this.attr("id")]) {
      $this.find("a[data-toggle=tab]:first, a[data-toggle=pill]:first").tab("show");
    }
  });
});