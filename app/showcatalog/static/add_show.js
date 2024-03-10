const add_show_form = document.getElementById("add-show-form")
add_show_form.addEventListener("submit", addShow)

/**
 * Update show information
 * @param {Event} event - The event of the update show form
 */
async function addShow(event) {
    event.preventDefault();

    const name = event.target[0].value
    const start_year = parseInt(event.target[1].value)
    const end_year = parseInt(event.target[2].value)
    const rating = parseFloat(event.target[3].value)
    const age_rating = event.target[4].value

    data = {
        name: name,
        start_year: start_year,
        end_year: end_year,
        rating: rating,
        age_rating: age_rating 
    }

    try {
        await fetch("/api/add-show", {
            method: "POST",
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