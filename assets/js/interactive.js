const headings = [...document.querySelectorAll("main h2, main h3")];
const toc = document.getElementById("toc");

if (toc && headings.length) {
    const title = document.createElement("h2");
    title.textContent = "Contents";
    const list = document.createElement("ul");

    headings.forEach((heading, index) => {
        if (!heading.id) {
            heading.id = `section-${index + 1}`;
        }

        const item = document.createElement("li");
        if (heading.tagName === "H3") {
            item.style.paddingLeft = "12px";
        }

        const link = document.createElement("a");
        link.href = `#${heading.id}`;
        link.textContent = heading.textContent;
        item.appendChild(link);
        list.appendChild(item);
    });

    toc.append(title, list);

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                const link = toc.querySelector(`a[href="#${entry.target.id}"]`);
                if (link) {
                    link.classList.toggle("active", entry.isIntersecting);
                }
            });
        },
        { rootMargin: "-20% 0px -65% 0px", threshold: 0.1 }
    );

    headings.forEach(heading => observer.observe(heading));
}

const lightbox = document.createElement("div");
lightbox.className = "lightbox";
lightbox.innerHTML = '<button type="button" aria-label="Close image">Close</button><img alt="">';
document.body.appendChild(lightbox);

const lightboxImage = lightbox.querySelector("img");
const closeLightbox = () => lightbox.classList.remove("open");

document.querySelectorAll("img.zoomable").forEach(image => {
    image.addEventListener("click", () => {
        lightboxImage.src = image.src;
        lightboxImage.alt = image.alt;
        lightbox.classList.add("open");
    });
});

lightbox.addEventListener("click", event => {
    if (event.target === lightbox || event.target.tagName === "BUTTON") {
        closeLightbox();
    }
});

document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
        closeLightbox();
    }
});

document.querySelectorAll(".footnote").forEach(footnote => {
    const note = footnote.dataset.note;
    if (note) {
        footnote.title = note;
    }
});
