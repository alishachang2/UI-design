$(document).ready(function () {
    console.log("ready!");
    const book = books.find(b => b.id == bookId)
    const similarIds = book.similar_book_ids;


    similarIds.forEach((id, index) => {
        const similarBook = books.find(b => b.id === id);
        document.getElementById(`similar-${index}`).innerHTML = `<p>${similarBook.title}</p><a href="/view/${similarBook.id}"><img src="${similarBook.cover}" width="100px"></a>`;
    });

    document.getElementById(`title`).textContent = book.title;
    document.getElementById(`image`).innerHTML = `<img src="${book.cover}" width="150px">`;
    document.getElementById('author').textContent = book.author.join(', ');
    document.getElementById('year').textContent = book.year;
    document.getElementById('score').textContent = `★ ${book.score}`;
    document.getElementById('summary').textContent = book.summary;
    document.getElementById('categories').innerHTML = book.category.map(c => `<span class="badge bg-secondary me-1">${c}</span>`).join('');
    document.getElementById('sub-categories').innerHTML = book.subcategory.map(b => `<span class="badge bg-secondary me-1">${b}</span>`).join('');
    document.getElementById('awards').innerHTML = book.awards.map(a => `<p>🏆 ${a}</p>`).join('');


    book.category.forEach(category => {
        console.log(category);
    });

});
