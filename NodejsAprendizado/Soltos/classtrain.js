class person{
    constructor(primeiro, segundo){
        this.firstname = primeiro;
        this.secondname = segundo;
        this.fullname = this.firstname+ " " + this.secondname;
    }

    dizer_nome(){
        return (`Ola meu nome é ${fullname}`);
    }
}


let newguy = new person("joao", "da silva");

console.log(newguy.dizer_nome());