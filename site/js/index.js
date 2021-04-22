function ext(){
    var time=[];
    var ecgValues=[];
    {% for data in datas %}
    var dates=new Date('{{ data.record_date}}');
    time.push(dates);
    ecgValues.push({{data.value}});
    {% endfor %}
    var ctx =document.getElementById("myChart");
    var myChart=new Chart( ctx, { type:'line', data:{labels:time, datasets:[{data:ecgValues, label:" ECG ", borderColor:"#324512", fill: false},]}});
    console.log(time)

}
