<event>
    <h5 id="headline">EVENT</h5>

    <script>
    this.on('mount', function() {

        console.log(opts)
        data = JSON.parse(JSON.stringify(opts))
        console.log(data)
        //this.headline.innerText = 'Event:' + data.date

    })
    </script>
</event>
