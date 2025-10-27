window.onload = function () {
    console.log("loaded script_get.js");
    document.querySelector("#insertPlantFormFetch").addEventListener("submit", async function (event) {
        event.preventDefault(); //save data
        console.log("button clicked");

        const htmlForm = document.querySelector("#insertPlantFormFetch"); //getting the data from the form
        const formData = new FormData(htmlForm); // take the form data and put it into a format that is understood
        //IMPORTANT:t the data must be formatted in a way that the server is capable of understanding 
        const queryParams = new URLSearchParams(formData).toString(); //helper function to help format the data =
        console.log(queryParams); //get info like this: o_name=Mars&a_name=Monstera&a_geo_loc=Canada&a_date=2025-09-29&a_descript=big+and+leafy

        const url = `/getDataFromForm?${queryParams}`;

        //prevent our website from crashing if there is an error in the url 
        // + communicate that to the user
        try {
            let res = await fetch(url)
            let resJSON = await res.json()
            console.log(resJSON)

            document.querySelector("#results").innerHTML += //append the page to respond to the data 
                `<p> THE NEW RESULT: <mark style = "background:orange">${resJSON.data_received}</mark></p>
                <p> THANK YOU : <mark style = "background:orange">${resJSON.owner}</mark></p>`
                //what appears on the page: 
                // RESULTS
                // THE NEW RESULT: success
                // THANK YOU: Mars

        }
        catch (err) {
            console.log(err)
        }


    })
}