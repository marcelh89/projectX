<eventlist>
    <h1 id="listname">Deathlist</h1>
    <newuser></newuser>
    <name  each={name in this.names} name={name} schrei={this.sayName}></name>

    <script>
    this.on('mount', function() {

        var randomnumber = Math.floor(Math.random() * (8000 - 3000 + 1)) + 1000;
        var intvalue = Math.round( randomnumber );
        console.log(intvalue)
        setTimeout(this.initvalues(), intvalue);
    })

    initvalues() {
        this.names = ['Bob', 'Alice']
        this.update()
    }

    addName(val) {
        this.names.push(val)
        this.update()
    }

    kill(val) {
        this.names.pop(val)
    }

    sayName(name) {
        console.log(name)
        this.listname.innerText = 'LoveList'
    }
    </script>
</eventlist>

<newuser>
    <h1>neuer name</h1>
    <input id=name type=text placeholder="Name"></input>
    <button onClick={neuerName}>Anlegen</button>

    <script>
        neuerName() {
            if (this.name.value.length > 0) {
                this.parent.addName(this.name.value)
            }
        }

    </script>
</newuser>

<name>
    <h1 onClick={los}>{opts.name}</h1>
    <button onClick={killme}>kill</button>

    <script>
    killme() {
        this.parent.kill(opts.name)
    }

    los() {
        opts.schrei('dont kill :' + opts.name)
    }
    </script>
</name>
