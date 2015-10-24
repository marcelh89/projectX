<event>
    <h5 id="headline">EVENT</h5>

    <script>
    this.on('mount', function() {

        //JSON.parse(opts.data) only by real json

        this.headline.innerText = this.headline.innerText + ' ' +  opts.data
    })
    </script>
</event>
