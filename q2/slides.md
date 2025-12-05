---
marp: true
theme: product-docs
paginate: true
header: "Product Documentation with Marp"
footer: "21f3000426@ds.study.iitm.ac.in"
---

<style>
/* @theme product-docs */

section {
  font-family: system-ui, sans-serif;
  background-color: #fdfdfd;
  color: #12212f;
  padding: 2.5rem;
}

section.lead h1 {
  font-size: 2.6rem;
  letter-spacing: 0.04em;
}

section::after {
  content: "Page " attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute;
  right: 1.8rem;
  bottom: 1.2rem;
  font-size: 0.75rem;
  opacity: 0.7;
}

code {
  background: #eef2ff;
  padding: 0.1em 0.3em;
  border-radius: 0.25rem;
}
</style>

_class: lead 

# Product Documentation with Marp  
**Author:** 21f3000426@ds.study.iitm.ac.in

---

## Why Marp?

- Markdown-based documentation  
- Version-controlled in Git  
- Export to HTML, PDF, Images  
- Reviewable via Pull Requests

---

## Repo Structure Example

```

docs/
slides.md
images/
architecture.png
README.md

````

---

## Custom Marp Directives

```markdown
marp: true
theme: product-docs
paginate: true
header: "Product Docs"
footer: "21f3000426@ds.study.iitm.ac.in"
````

---

<!-- _class: lead -->
<!-- backgroundImage: "url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80')" -->
<!-- backgroundSize: cover -->
<!-- backgroundPosition: center -->
<!-- color: #ffffff -->

# System Overview

Microservice-based SaaS product
API-first and scalable

---

## Math & Complexity

$T(n) = O(n)$

$T(n) = 2T(n/2) + O(n) = O(n \log n)$

Query time: $O(\log n + k)$

---

## Contact

**[21f3000426@ds.study.iitm.ac.in](mailto:21f3000426@ds.study.iitm.ac.in)**

---

## Summary

* Custom theme
* Background image
* Math equations
* Page numbers
* Git-friendly documentation

---