function toggleDropdown() {
    let dropdown_display_status = document.getElementById('dropdown').style.display;
    if (dropdown_display_status == 'none') {
        document.getElementById('dropdown').style.display = 'block'
    }
    else {
        document.getElementById('dropdown').style.display = 'none'
    }
}

/**
 * Delete
 * @param {Number} id - The id of the show
 */
async function deleteShow(id) {
    const confirm_action = confirm("Do you really want to delete the show!");

    if (confirm_action === true) {
        try {
            await fetch("/api/delete-show?show_id=" + id, {
                method: "DELETE",
            })
            location.reload();
        } catch (error) {
            console.error("Error: " + error)
        }
    }
}

