let counter = 1;

const intervalId = setInterval(() => {
    console.log(`Hello world for the ${counter} time!`);
    counter++;

    if(counter >= 6){
        console.log('done!');
        clearInterval(intervalId);
    }
},1000);