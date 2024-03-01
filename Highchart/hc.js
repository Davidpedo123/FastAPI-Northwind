fetch('http://127.0.0.1:8000/Orders')
    .then(response => response.json())
    .then(data => {
        // Aquí puedes llamar a la función que crea el gráfico, pasando los datos
        crearGrafico(data);
    });

function crearGrafico(data) {
    Highcharts.chart('myChart', {  // Cambia 'container' a 'myChart'
        chart: {
            type: 'pie'  // Cambia 'column' a 'pie' para un gráfico de pastel
        },
        title: {
            text: 'Ordenes por City'
        },
        series: [{
            name: 'Órdenes',
            data: data.map(item => ({
                name: item.ship_city,
                y: item.city_count
            }))
        }]
    });
}
