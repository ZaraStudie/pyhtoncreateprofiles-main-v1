const allMoviesTBody = document.querySelector("#allItems tbody")

const showTable = function(moviesArray){
    allMoviesTBody.innerHTML = ""
    for(let i = 0; i < moviesArray.length;i++) { 
        let trText = `<tr><th scope="row">${moviesArray[i].Givenname} ${moviesArray[i].Surname}</th><td>${moviesArray[i].Country}</td><td>${moviesArray[i].Birthday.substring(0,4)}</td></tr>`
        allMoviesTBody.innerHTML += trText
    }

} 

fetch('./data.json')
    .then((response) => response.json())
    .then((json) => {
        showTable(json)
    });
