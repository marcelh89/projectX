<eventlist>
    <h1>EventList</h1>
    <event each={this.events} data={this}></event>

    <script>
    this.on('mount', function() {
        console.log(opts)
        urlwithid =  "api/randomevents?id=" + opts.id
        var that = this
        $.ajax({
            method: "GET",
            url: urlwithid
        })
        .done(function( uploadsData ) {
            responseData = JSON.parse(uploadsData)
            console.log(responseData)
            that.events = responseData.dates
            that.update()
        });
    })
    </script>
</eventlist>

<event>
    <h5 id="headline">EVENT</h5>
    <script>
        this.on('mount', function() {
            this.headline.innerText = 'Event ' +  opts.data.date
        })
    </script>
</event>
