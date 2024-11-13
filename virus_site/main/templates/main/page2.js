document.querySelectorAll('.filter-toggle').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
        button.classList.toggle('expanded');
    });
});

const data = [
    {
      sNo: "1",
      accessionNo: "YP_010839200RefSeq",
      organismName: "Orthohantavirus puumalaense",
      vrl: "6/5/2023",
      species: "Orthohantavirus puumalaense",
      length: "433",
      geoLocation: "Australia",
      host: "Peromyscus maniculatus",
      collectionDate: "3/7/2017"
    },
    {
      sNo: "2",
      accessionNo: "YP_010839201RefSeq",
      organismName: "Orthohantavirus sinnombreense",
      vrl: "6/5/2023",
      species: "Orthohantavirus sinnombreense",
      length: "428",
      geoLocation: "United Kingdom",
      host: "Pteropus alecto",
      collectionDate: "2014"
    },
    {
      sNo: "3",
      accessionNo: "YP_010088055RefSeq",
      organismName: "Orthohantavirus robinaense",
      vrl: "1/6/2021",
      species: "Orthohantavirus robinaense",
      length: "429",
      geoLocation: "Czech Republic",
      host: "Microtus agrestis",
      collectionDate: "2010"
    },
    {
      sNo: "4",
      accessionNo: "YP_010088057RefSeq",
      organismName: "Orthohantavirus tatenalense",
      vrl: "1/6/2021",
      species: "Orthohantavirus tatenalense",
      length: "433",
      geoLocation: "USA",
      host: "Sorex minutus",
      collectionDate: "11/9/2003"
    },
    {
      sNo: "5",
      accessionNo: "YP_00964722RefSeq",
      organismName: "Orthohantavirus asikkalaense",
      vrl: "28/6/2019",
      species: "Orthohantavirus asikkalaense",
      length: "429",
      geoLocation: "Colombia: Antioquia",
      host: "Neurotrichus gibbsii",
      collectionDate: "7/2/2011"
    },
    {
      sNo: "6",
      accessionNo: "YP_00965159RefSeq",
      organismName: "Oxbow virus",
      vrl: "28/6/2019",
      species: "Orthohantavirus oxbowense",
      length: "428",
      geoLocation: "Finland",
      host: "Zygodontomys brevicauda",
      collectionDate: ""
    },
    {
      sNo: "7",
      accessionNo: "YP_00966011RefSeq",
      organismName: "Necocli virus",
      vrl: "28/6/2019",
      species: "Orthohantavirus neococliense",
      length: "428",
      geoLocation: "Japan",
      host: "Sorex araneus",
      collectionDate: ""
    },
    {
      sNo: "8",
      accessionNo: "YP_00966652RefSeq",
      organismName: "Seewis virus",
      vrl: "28/6/2019",
      species: "Seewis orthohantavirus",
      length: "429",
      geoLocation: "Australia",
      host: "Peromyscus maniculatus",
      collectionDate: "3/7/2017"
    },
    {
      sNo: "9",
      accessionNo: "YP_009505459RefSeq",
      organismName: "Asama virus",
      vrl: "24/8/2018",
      species: "Orthohantavirus asamaense",
      length: "433",
      geoLocation: "United Kingdom",
      host: "Pteropus alecto",
      collectionDate: "2014"
    },
    {
      sNo: "10",
      accessionNo: "YP_009505595RefSeq",
      organismName: "Orthohantavirus bayoui",
      vrl: "24/8/2018",
      species: "Orthohantavirus bayoui",
      length: "433",
      geoLocation: "Czech Republic",
      host: "Microtus agrestis",
      collectionDate: "2010"
    }
  ];
  
  const tableBody = document.querySelector("#dataTable tbody");
  
  data.forEach(row => {
    const tr = document.createElement("tr");
  
    // Create and append cells to the row
    for (const key in row) {
      const td = document.createElement("td");
      td.textContent = row[key];
      tr.appendChild(td);
    }
  
    // Append the row to the table body
    tableBody.appendChild(tr);
  });
  