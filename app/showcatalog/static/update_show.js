window.onload = (event) => {
    const params = new URLSearchParams(location.search)
    const id = params.get("id")

    if (id === null || id === '') {
        location.href = "/dashboard"
    }

    getShowInfo(id).then((data) => {
        console.log(data)
        document.getElementById("name").value = data.name;
        document.getElementById("start-year").value = data.start_year;
        document.getElementById("end-year").value = data.end_year;
        document.getElementById("rating").value = data.rating;
        document.getElementById("age-rating").value = data.age_rating;
    })
}


/**
 * Get show data
 * @param {number} id - The id of the show
 */
async function getShowInfo(id) {
    try {
        const response = await fetch("/api/fetch-show?show_id=" + id, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })
        return response.json();
    } catch (error) {
        console.error("Error: " + error)
    }
}

const update_show_form = document.getElementById("update-show-form")
update_show_form.addEventListener("submit", updateShowInfo)

/**
 * Update show information
 * @param {Event} event - The event of the update show form
 */
async function updateShowInfo(event) {
    event.preventDefault();

    const params = new URLSearchParams(location.search)

    const show_id = parseInt(params.get("id"))
    const name = event.target[0].value
    const start_year = parseInt(event.target[1].value)
    const end_year = parseInt(event.target[2].value)
    const rating = parseFloat(event.target[3].value)
    const age_rating = event.target[4].value

    data = {
        show_id: show_id,
        name: name,
        start_year: start_year,
        end_year: end_year,
        rating: rating,
        age_rating: age_rating 
    }

    try {
        await fetch("/api/update-show", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        location.href = "/dashboard"
    } catch (error) {
        console.error("Error: " + error)
    }
}





