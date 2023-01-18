const CONF = {
    apiUrl: 'http://localhost:8000/api'
}

const getApplicants = async () => {
    console.log('Here in the api call')
    const response = await fetch(`${CONF.apiUrl}/applicant`)
    const data = await response.json()
    console.log(data)
    console.log("I called")
    return data
    
}

const buildTable = (responseJson, keys) => {
    const scope_table = document.getElementById('scope_table')
    scope_table.innerHTML = ""
    const table = document.createElement('table')
    table.id = "my_table"
    const tr = document.createElement('tr')
    tr.classList.add("bg-info")
    table.classList.add('table')
    table.classList.add('table-striped')
    
    scope_table.appendChild(table)
    if (responseJson.length === 0) {
        const p = document.createElement('p')
        p.innerText = "No data of user with techs"
        table.appendChild(p)
        return 
    }

    for (let index = 0; index < keys.length; index++) {
        const th = document.createElement('th')
        th.innerText = `${keys[index]}`
        tr.appendChild(th)
    }

    const tbody = document.createElement('tbody')

    for (let i = 0; i < responseJson.length; i++){
            const tr = document.createElement('tr')
            for (let j = 0; j < keys.length; j++) {
                const td = document.createElement('td');
                td.innerHTML = `${responseJson[i][keys[j]] || 'Not info'}`
                tr.appendChild(td)
            }
			tbody.appendChild(tr)

		}
        
    table.appendChild(tr)
    table.appendChild(tbody)
}

const getApplicantsAndBuildTable = async () => {
    const data = await getApplicants()
    buildTable(data, Object.keys(data[0]))
}

const getApplicantsWithTechExperienceAndBuildTable = async () => {
    const data = await getApplicants()
    const keys = Object.keys(data[0])
    for (let index = 0; index < data.length; index++) {
        const applicant_id = data[index].id;
        const response = await fetch(
            `${CONF.apiUrl}/technology-experience/get-techs-experience-by-applicant?applicant_id=${applicant_id}`
            )
        const responseJson = await response.json()
        if (responseJson.length === 0) {
            data.pop(index)
        }
        for (let j = 0; j < responseJson.length; j++) {
            const tech_relation = responseJson[j] 
            data[index][`${tech_relation.tech_name}`] = tech_relation.experience
            if (!keys.includes(`${tech_relation.tech_name}`)) {
                keys.push(tech_relation.tech_name)
            }
        }
        
    }

    buildTable(data, keys)
    
}

/* const getTechsWithExperienceAndBuildTable = async () => {
    const 
} */

const fillTechOptions = async (id) => {
    const select = document.getElementById(id);
    const data = await fetch(`${CONF.apiUrl}/technology`)
    const techList = await data.json()
    techList.forEach((tech) => {
        const option = document.createElement('option')
        option.value = tech.id
        option.innerHTML = `${tech.tech_name}`
        select.appendChild(option)
     })
}

const avoidRefresh = (idForm) => {
    form = document.getElementById(idForm);
    const handleForm = (event) => { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);
}

const initPage = (idSelect, idForm) => {
    fillTechOptions(idSelect)
    avoidRefresh(idForm)
} 

const getExperienceByTech = async (selectId) => {
    
    const select = document.getElementById(selectId)
    const id_tech = select.options[select.selectedIndex].value
    const url = `${CONF.apiUrl}/technology-experience/get-applicant-experience-by-tech?tech_id=${id_tech}`
    const response = await fetch(
            url
        )
    const responseJson = await response.json()
    return responseJson
}

const getExperienceByTechAndBuildTable = async (selectId) => {
    responseJson = await getExperienceByTech(selectId)
    buildTable(responseJson, Object.keys(responseJson[0]))
}

const pdfExport = (id) => {
    const pdf = new jsPDF('p', 'pt', 'letter');
    // source can be HTML-formatted string, or a reference
    // to an actual DOM element from which the text will be scraped.
    const table = document.getElementById(id);

    margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case
    pdf.fromHTML(
        table, // HTML string or DOM elem ref.
        margins.left, // x coord
        margins.top, { // y coord
            'width': margins.width // max width of content on PDF
        },

        function (dispose) {
            // dispose: object with X, Y of the last line add to the PDF 
            //          this allow the insertion of new lines after html
            pdf.save('Report.pdf');
        }, 
        margins
    );
}