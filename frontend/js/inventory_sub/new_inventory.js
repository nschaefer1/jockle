


async function init(api) {
    window.api = api;
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