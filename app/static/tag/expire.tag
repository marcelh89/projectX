<expire>

    <button onClick={createItem}>Create Item</button>

    <table class="table">
        <tr each={item in this.items}>
            <td>{item.message}</td>
            <td>{item.created}</td>
        </tr>
    </table>

    <script>
    this.on('mount', function() {
        this.interval = setInterval(this.getItems, 1500);
    })

    this.on('unmount', function() {
        window.clearInterval(this.interval)
    })

    createItem() {

        var val = 'NewItem'
        var saveData = $.ajax({
            type: 'POST',
            url: "api/shotitems/",
            data: {
                'val': val,
                dataType: "text"},
            success: function (resultData) {
                console.log(resultData)
            }
        });
        saveData.error(function () {
            console.error("Something went wrong");
        });
    }

    getItems() {
        var that = this;
        var ajax = $.ajax({
            type: 'GET',
            url: "api/shotitems/",
            success: function (resultData) {
                that.items = JSON.parse(resultData)
                that.update()
            }
        });
        ajax.error(function () {
            console.error("Something went wrong");
        });

    }
    </script>
</expire>

