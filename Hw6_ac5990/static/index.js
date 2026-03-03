$(document).ready(function () {
    console.log("ready!");
    const ids = [2, 5, 9];

    ids.forEach((id, index) => {
        const book = books.find(b => b.id === id);
        document.getElementById(`pop-item-${index + 1}`).innerHTML = `<p>${book.title}</p><a href="/view/${book.id}"><img src="${book.cover}" width="100px"></a>`;
    });

});
