

async function init(api) {

    // Grab the item list from the API
    let sel_char_ck = await api.get_session('sel_char_ck');
    let response = await api.getItemList(sel_char_ck);
    if (!response.success) {
        console.log('API Call Failed');
        // TODO add error message in container if possible
        return
    };

    // Log the API call success
    console.log('API call successful');

    // Populate the container with the div elements
    const container = document.getElementById('inventory-list');
    response.data.forEach(item => {
        // Create a div element of the item-bar
        const item_bar = document.createElement('div');
        item_bar.className = 'item-bar';
        item_bar.setAttribute('data-name', item.inv_name);

        // Create a img element for item-bar-icon
        const img = document.createElement('img'); 
        img.className = 'item-bar-icon';
        img.src = `../../assets/icons/${item.icon_path ?? "uncertainty.png"}`;
        item_bar.appendChild(img)

        // Create a div element for the item-bar-name
        const item_bar_name = document.createElement('div');
        item_bar_name.className = 'item-bar-name';
        item_bar_name.textContent = item.inv_name;
        item_bar.appendChild(item_bar_name);

        // Create a div element for the item-bar-count
        const item_bar_count = document.createElement('div');
        let formatted_num = '';
        item_bar_count.className = 'item-bar-count';
        if (item.item_count >= 1000000) {
            formatted_num = (item.item_count/1000000).toFixed(1) + "M";
        } else if (item.item_count >= 1000) {
            formatted_num = (item.item_count/1000).toFixed(1) + "K";
        } else {
            formatted_num = item.item_count;
        }
        item_bar_count.textContent = `Current Count: ${formatted_num}`;
        item_bar.appendChild(item_bar_count);

        // Add the click listener for the item-bar
        item_bar.addEventListener('click', () => {
            console.log('Clicked item: ', item.inv_ck);
            // Remove any selected elements
            document.querySelectorAll('.item_bar').forEach(bar => {
                bar.classList.remove('selected');
            });
            // Trigger selection
            item_bar.classList.add('selected');
            // Show the stuff in the details container
            const details_container = document.getElementById('details-area');
            details_container.classList.remove('hidden');
            // Clear HTML content
            details_container.innerHTML = ``;
            details_container. innerHTML = `
                <h2>${item.inv_name}</h2>
                <p>${item.inv_desc}</p>
            `;
        });

        // Add the item-bar to the main container
        container.appendChild(item_bar);
    });



    // Search bar event listener
    document.getElementById('inventory-search').addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();

        document.querySelectorAll('.item-bar').forEach(bar => {
            bar.classList.remove('selected');
            const name = bar.getAttribute('data-name')?.toLowerCase() ?? "";
            bar.style.display = name.includes(term) ? 'flex' : 'none';
        });
    });

    // Search bar clear event listener
    const search_input = document.getElementById('inventory-search');
    const clearBtn = document.getElementById('clear-search');
    clearBtn.addEventListener('click', () => {
        search_input.value = "";
        search_input.dispatchEvent(new Event('input')); // reruns the filter logic
    });
    
}


window.addEventListener('pywebviewready', () => {
    let api = window.pywebview.api; // alias the API
    init(api);
});

// FUNCTIONS FOR JS
async function uploadBtnPress() {
    const uploader = document.getElementById('file-input');
    const file = uploader.files[0];

    if (!file) {
        console.log('Upload button pressed, no file found');
        return;
    }

    const reader = new FileReader();
    reader.onload = async () => {
        const base64 = reader.result.split(",")[1];
        response = await api.receive_png_base64(file.name, base64);
        if (!response.success) {
                console.log('API call failed: trying to upload PNG to icons/custom');
                //TODO add error message in container if possible
                return
            }
            console.log('API call successful: uploaded PNG to icons/custom')

        };

        reader.readAsDataURL(file);
    };