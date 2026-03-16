---
url: /community-contributors.html
title: Contributors
keywords: contributors, developers, maintainers
summary:
toc: true
---

## Maintainers

<br>
{{- $dev_main := .Site.Data.developer.main  | sort "name" -}}
<div class="row">
<div class="col-md-10 offset-md-1">
<ul class="devlist">
  {{- range $loop, $p := dev_main -}}
  <li{{- if $loop.IsFirst -}} class="devlist-first"{{- end -}}>
    <div class="devlist-img">
      {{- if p.img -}}
      <img src="images/developer/{{ p.img }}.jpg" alt="Portrait">
      {{- end -}}
    </div>
    <div class="devlist-left">
      <p>
        <strong>{{ p.fullname }}</strong><br/>
        {{ p.institution }}
      </p>
    </div>
    <ul class="devlist-right">
      {{- if p.orcid -}}<li><a href="{{ p.orcid }}" alt="See the institutional website" class="no-icon"><i class="fab fa-orcid"></i></a></li>{{- end -}}
      {{- if p.github -}}<li><a href="https://github.com/{{ p.github }}" alt="See the Github profile" class="no-icon"><i class="fab fa-github"></i></a></li>{{- end -}}
    </ul>
  </li>
  {{- end -}}
</ul>
</div>
</div>

If you are interested in joining the team of preCICE maintainers, please [contact Benjamin Uekermann](https://www.ipvs.uni-stuttgart.de/departments/us3/).

## Previous maintainers

Previous mantainers and their affiliation at the time of their last significant contribution.

<br>
{{- $dev_premain := .Site.Data.developer.main-inactive  | sort "name" -}}
<div class="row">
<div class="col-md-10 offset-md-1">
<ul class="devlist">
  {{- range $loop, $p := dev_premain -}}
  <li{{- if $loop.IsFirst -}} class="devlist-first"{{- end -}}>
    <div class="devlist-left">
      <p>
        <strong>{{ p.fullname }}</strong><br/>
        {{ p.institution }}
      </p>
    </div>
    <ul class="devlist-right">
      {{- if p.orcid -}}<li><a href="{{ p.orcid }}" alt="See the institutional website" class="no-icon"><i class="fab fa-orcid"></i></a></li>{{- end -}}
      {{- if p.github -}}<li><a href="https://github.com/{{ p.github }}" alt="See the Github profile" class="no-icon"><i class="fab fa-github"></i></a></li>{{- end -}}
    </ul>
  </li>
  {{- end -}}
</ul>
</div>
</div>

## Further contributors

Previous contributors and their affiliation at the time of their last significant contribution.

<br>
{{- $dev_contrib := .Site.Data.developer.contributors  | sort "name" -}}
<div class="row">
<div class="col-md-10 offset-md-1">
<ul class="devlist">
  {{- range $loop, $p := dev_contrib -}}
  <li{{- if $loop.IsFirst -}} class="devlist-first"{{- end -}}>
    <div class="devlist-left">
      <p>
        <strong>{{ p.fullname }}</strong><br/>
        {{ p.institution }}
      </p>
    </div>
    <ul class="devlist-right">
      {{- if p.orcid -}}<li><a href="{{ p.orcid }}" alt="See the institutional website" class="no-icon"><i class="fab fa-orcid"></i></a></li>{{- end -}}
      {{- if p.github -}}<li><a href="https://github.com/{{ p.github }}" alt="See the Github profile" class="no-icon"><i class="fab fa-github"></i></a></li>{{- end -}}
    </ul>
  </li>
  {{- end -}}
</ul>
</div>
</div>
