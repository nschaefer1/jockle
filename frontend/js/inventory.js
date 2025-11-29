
async function handleItemClick(inv_ck, inv_name, inv_desc) {
    

}

async function init(api) {
    
    // SELECT A DUMMY CHARACTER
    // TODO remove this line once we have character section
    await api.set_session('sel_char_ck', 1) // SELECTING VEYRA

    // POPULATE THE INVENTORY
    let sel_char_ck = await api.get_session('sel_char_ck')
    let response = await api.getInventory(sel_char_ck)
    if (!response.success) {
        console.log('API Call Failed')
        // TODO add error message in the container if possible
        return
    }

    console.log('API call successful');
    let container = document.getElementById('inventory-area');
    response.data.forEach(item => {

        // Creating a div element to add
        const div = document.createElement('div');

        // Attributes of the div element
        div.className = 'card';
        div.setAttribute('data-name', item.inv_name)

        // Creating img element
        const img = document.createElement('img');
        let img_path = `../assets/icons/${item.icon_path ?? "uncertainty.png"}`;
        img.src = img_path;
        img.className = 'card-icon';
        // Add img to container
        div.appendChild(img);

        // Creating the count variable at the bottomr ight
        const num = document.createElement('div');
        if (item.item_count >= 1000000) {
            num.textContent = (item.item_count/1000000).toFixed(1) + "M";
        } else if (item.item_count >= 1000) {
            num.textContent = (item.item_count/1000).toFixed(1) + "K";
        } else {
            num.textContent = item.item_count;
        }
        num.className = 'card-num';
        // Add the number to the div
        div.appendChild(num);

        // CLICK events
        div.addEventListener('click', () => {
            console.log('Clicked item: ', item.inv_ck);
            // Show the details container
            const details_container = document.getElementById('details-area');
            details_container.classList.remove('hidden');
            // Clear HTML content
            details_container.innerHTML = ``;
            details_container.innerHTML = `
                <h2>${item.inv_name}</h2>
                <p>${item.inv_desc}</p>
            `;
        });

        // HOVER Events
        div.addEventListener('mouseenter', () => {
            tooltip.innerHTML = `
                <strong>${item.inv_name}</strong><br>
                <p>${item.inv_desc}</p>
            `;
            tooltip.style.visibility = "visible";
            tooltip.style.opacity = "1";
        });
        div.addEventListener('mousemove', (e) => {
            const tooltipWidth = tooltip.offsetWidth;
            const margin = 12;
            
            let left = e.pageX + margin;

            if (left + tooltipWidth > window.innerWidth) {
                left = e.pageX - tooltipWidth - margin;
            }
            tooltip.style.left = left + 'px';
            tooltip.style.top = (e.pageY + margin) + 'px';
        });
        div.addEventListener('mouseleave', () => {
            tooltip.style.visibility = "hidden";
            tooltip.style.opacity = "0";
        });

        // Add card to container
        container.appendChild(div);

    });

    // ADD SEARCH BAR EVENT LISTENER
    document.getElementById('inventory-search').addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();

        document.querySelectorAll('.card').forEach(card => {
            const name = card.getAttribute('data-name')?.toLowerCase() ?? "";
            card.style.display = name.includes(term) ? 'flex' : 'none';
        });
    });

    // CLEAR BTN EVENT LISTENER
    const search_input = document.getElementById('inventory-search');
    const clearBtn = document.getElementById('clear-search')
    clearBtn.addEventListener('click', () => {
        search_input.value = "";
        search_input.dispatchEvent(new Event('input')); // reruns the filter logic
    });
}

window.addEventListener('pywebviewready', () => {
    let api = window.pywebview.api; // alias the API
    init(api);
});
