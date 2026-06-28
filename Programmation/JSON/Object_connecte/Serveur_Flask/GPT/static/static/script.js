async function lireEtat(){

    let r = await fetch("/etat");

    let data = await r.json();

    document.getElementById("etat").innerHTML=data.bouton;

    if(data.bouton=="ON"){

        document.getElementById("lampe").style.background="lime";

    }

    else{

        document.getElementById("lampe").style.background="red";

    }

}

async function changerEtat(){

    let r=await fetch("/etat");

    let data=await r.json();

    let nouvelEtat;

    if(data.bouton=="OFF")
        nouvelEtat="ON";
    else
        nouvelEtat="OFF";

    await fetch("/etat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            bouton:nouvelEtat
        })

    });

    lireEtat();

}

setInterval(lireEtat,1000);

lireEtat();
