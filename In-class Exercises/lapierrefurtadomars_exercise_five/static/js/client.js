/* PLEASE DO NOT CHANGE THIS FRAMEWORK ....
the get requests are all implemented and working ... 
so there is no need to alter ANY of the existing code: 
rather you just ADD your own ... */

window.onload = function () {
  document.querySelector("#queryChoice").selectedIndex = 0;
  //create once :)
  let description = document.querySelector("#Ex4_title");
  //array to hold the dataPoints
  let dataPoints = [];

  // /**** GeT THE DATA initially :: default view *******/
  // /*** no need to change this one  **/
  runQueryDefault("onload");

  /***** Get the data from drop down selection ****/
  let querySelectDropDown = document.querySelector("#queryChoice");

  querySelectDropDown.onchange = function () {
    console.log(this.value);
    let copyVal = this.value;
    console.log(copyVal);
    runQuery(copyVal);
  };

  /******************* RUN QUERY***************************  */
  async function runQuery(queryPath) {
    // // //build the url -end point
    const url = `/${queryPath}`;
    try {
      let res = await fetch(url);
      let resJSON = await res.json();
      console.log(resJSON);

      //reset the
      document.querySelector("#childOne").innerHTML = "";
      description.textContent = "";
      document.querySelector("#parent-wrapper").style.background =
        "rgba(51,102,255,.2)";

      switch (queryPath) {
        case "default": {
          displayAsDefault(resJSON);
          break;
        }
        case "one": {
          //sabine done
          displayInCirclularPattern(resJSON);
          break;
        }
        case "two": {
          //sabine done
          displayByGroups(resJSON, "weather", "eventName");
          break;
        }
        /***** TO DO FOR EXERCISE 4 *************************
         ** 1: Once you have implemented the mongodb query in server.py,
         ** you will receive it from the get request (THE FETCH HAS ALREADY BEEN IMPLEMENTED:: SEE ABOVE) 
         ** and will automatically will enter into the correct select case
         **  - based on the value that the user chose from the drop down list...)
         ** You need to design and call a custom display function FOR EACH query that you construct ...
         ** 4 queries - I want 4 UNIQUE display functions - you can use the ones I created
         ** as inspiration ONLY - DO NOT just copy and change colors ... experiment, explore, change ...
         ** you can create your own custom objects - but NO images, video or sound... (will get 0).
         ** bonus: if your visualizations(s) are interactive or animate.
         ****/
        case "three": {
          console.log("three")
          visualizeThree(resJSON);
          break;
        }
        case "four": {
          console.log("four")
          visualizeFour(resJSON);
          break;
        }

        case "five": {
          console.log("five")
          visualizeFive(resJSON);
          break;
        }
        case "six": {
          console.log("six")
          visualizeSix(resJSON);
          break;
        }
        default: {
          console.log("default case");
          break;
        }
      } //switch
    } catch (err) {
      console.log(err);
    }
  }
  //will make a get request for the data ...

  /******************* RUN DEFAULT QUERY***************************  */
  async function runQueryDefault(queryPath) {
    // // //build the url -end point
    const url = `/${queryPath}`;
    try {
      let res = await fetch(url);
      let resJSON = await res.json();
      console.log(resJSON);
      displayAsDefault(resJSON);
    } catch (err) {
      console.log(err);
    }
  }
  /*******************DISPLAY AS GROUP****************************/

  function displayByGroups(resultObj, propOne, propTwo) {
    dataPoints = [];
    let finalHeight = 0;
    //order by WEATHER and Have the event names as the color  ....

    //set background of parent ... for fun ..
    document.querySelector("#parent-wrapper").style.background =
      "rgba(51, 153, 102,1)";
    description.textContent = "BY WEATHER AND ALSO HAVE EVENT NAMES {COLOR}";
    description.style.color = "rgb(179, 230, 204)";

    let coloredEvents = {};
    let resultSet = resultObj.results;

    //reget
    let possibleEvents = resultObj.events;
    let possibleColors = [
      "rgb(198, 236, 217)",
      "rgb(179, 230, 204)",
      "rgb(159, 223, 190)",
      "rgb(140, 217, 177)",
      "rgb(121, 210, 164)",
      "rgb(102, 204, 151)",
      "rgb(83, 198, 138)",
      "rgb(64, 191, 125)",
      "rgb(255, 204, 179)",
      "rgb(255, 170, 128)",
      "rgb(255, 153, 102)",
      "rgb(255, 136, 77)",
      "rgb(255, 119, 51)",
      "rgb(255, 102, 26)",
      "rgb(255, 85, 0)",
      "rgb(230, 77, 0)",
      "rgb(204, 68, 0)",
    ];

    for (let i = 0; i < possibleColors.length; i++) {
      coloredEvents[possibleEvents[i]] = possibleColors[i];
    }

    let offsetX = 20;
    let offsetY = 150;
    // find the weather of the first one ...
    let currentGroup = resultSet[0][propOne];
    console.log(currentGroup);
    let xPos = offsetX;
    let yPos = offsetY;

    for (let i = 0; i < resultSet.length - 1; i++) {
      dataPoints.push(
        new myDataPoint(
          resultSet[i].dataId,
          resultSet[i].day,
          resultSet[i].weather,
          resultSet[i].start_mood,
          resultSet[i].after_mood,
          resultSet[i].after_mood_strength,
          resultSet[i].event_affect_strength,
          resultSet[i].event_name,
          //map to the EVENT ...
          coloredEvents[resultSet[i].event_name],
          //last parameter is where should this go...
          document.querySelector("#childOne"),
          //which css style///
          "point_two"
        )
      );

      /** check if we have changed group ***/
      if (resultSet[i][propOne] !== currentGroup) {
        //update
        currentGroup = resultSet[i][propOne];
        offsetX += 150;
        offsetY = 150;
        xPos = offsetX;
        yPos = offsetY;
      }
      // if not just keep on....
      else {
        if (i % 10 === 0 && i !== 0) {
          xPos = offsetX;
          yPos = yPos + 15;
        } else {
          xPos = xPos + 15;
        }
      } //end outer else

      dataPoints[i].update(xPos, yPos);
      finalHeight = yPos;
    } //for

    document.querySelector("#childOne").style.height = `${finalHeight + 20}px`;
  } //function

  /*****************DISPLAY IN CIRCUlAR PATTERN:: <ONE>******************************/
  function displayInCirclularPattern(resultOBj) {
    //reset
    dataPoints = [];
    let xPos = 0;
    let yPos = 0;
    //for circle drawing
    let angle = 0;
    let centerX = window.innerWidth / 2;
    let centerY = 350;

    let scalar = 300;
    let yHeight = Math.cos(angle) * scalar + centerY;

    let resultSet = resultOBj.results;
    let coloredMoods = {};

    let possibleMoods = resultOBj.moods;
    let possibleColors = [
      "rgba(0, 64, 255,.5)",
      "rgba(26, 83, 255,.5)",
      "rgba(51, 102, 255,.7)",
      "rgba(51, 102, 255,.4)",
      "rgba(77, 121,255,.6)",
      "rgba(102, 140, 255,.6)",
      "rgba(128, 159, 255,.4)",
      "rgba(153, 179, 255,.3)",
      "rgba(179, 198, 255,.6)",
      "rgba(204, 217, 255,.4)",
    ];

    for (let i = 0; i < possibleMoods.length; i++) {
      coloredMoods[possibleMoods[i]] = possibleColors[i];
    }

    //set background of parent ... for fun ..
    document.querySelector("#parent-wrapper").style.background =
      "rgba(0, 26, 102,1)";
    description.textContent = "BY AFTER MOOD";
    description.style.color = "rgba(0, 64, 255,.5)";

    for (let i = 0; i < resultSet.length - 1; i++) {
      dataPoints.push(
        new myDataPoint(
          resultSet[i].dataId,
          resultSet[i].day,
          resultSet[i].weather,
          resultSet[i].start_mood,
          resultSet[i].after_mood,
          resultSet[i].after_mood_strength,
          resultSet[i].event_affect_strength,
          resultSet[i].event_name,
          //map to the day ...
          coloredMoods[resultSet[i].after_mood],
          //last parameter is where should this go...
          document.querySelector("#childOne"),
          //which css style///
          "point_two"
        )
      );
      /*** circle drawing ***/
      xPos = Math.sin(angle) * scalar + centerX;
      yPos = Math.cos(angle) * scalar + centerY;
      angle += 0.13;

      if (angle > 2 * Math.PI) {
        angle = 0;
        scalar -= 20;
      }
      dataPoints[i].update(xPos, yPos);
    } //for

    document.querySelector("#childOne").style.height = `${yHeight}px`;
  } //function

  /*****************DISPLAY AS DEFAULT GRID :: AT ONLOAD ******************************/
  function displayAsDefault(resultOBj) {
    //reset
    dataPoints = [];
    let xPos = 0;
    let yPos = 0;
    const NUM_COLS = 50;
    const CELL_SIZE = 20;
    let coloredDays = {};
    let resultSet = resultOBj.results;
    possibleDays = resultOBj.days;
    /*
  1: get the array of days (the second entry in the resultOBj)
  2: for each possible day (7)  - create a key value pair -> day: color and put in the
  coloredDays object
  */
    console.log(possibleDays);
    let possibleColors = [
      "rgb(255, 102, 153)",
      "rgb(255, 77, 136)",
      "rgb(255, 51, 119)",
      "rgb(255, 26, 102)",
      "rgb(255, 0, 85)",
      "rgb(255, 0, 85)",
      "rgb(255, 0, 85)",
    ];

    for (let i = 0; i < possibleDays.length; i++) {
      coloredDays[possibleDays[i]] = possibleColors[i];
    }
    /* for through each result
    1: create a new MyDataPoint object and pass the properties from the db result entry to the object constructor
    2: set the color using the coloredDays object associated with the resultSet[i].day
    3:  put into the dataPoints array.
    **/
    //set background of parent ... for fun ..
    document.querySelector("#parent-wrapper").style.background =
      "rgba(255,0,0,.4)";
    description.textContent = "DEfAULT CASE";
    description.style.color = "rgb(255, 0, 85)";

    //last  element is the helper array...
    for (let i = 0; i < resultSet.length - 1; i++) {
      dataPoints.push(
        new myDataPoint(
          resultSet[i].dataId,
          resultSet[i].day,
          resultSet[i].weather,
          resultSet[i].start_mood,
          resultSet[i].after_mood,
          resultSet[i].after_mood_strength,
          resultSet[i].event_affect_strength,
          resultSet[i].evnet_name,
          //map to the day ...
          coloredDays[resultSet[i].day],
          //last parameter is where should this go...
          document.querySelector("#childOne"),
          //which css style///
          "point"
        )
      );

      /** this code is rather brittle - but does the job for now .. draw a grid of data points ..
//*** drawing a grid ****/
      if (i % NUM_COLS === 0) {
        //reset x and inc y (go to next row)
        xPos = 0;
        yPos += CELL_SIZE;
      } else {
        //just move along in the column
        xPos += CELL_SIZE;
      }
      //update the position of the data point...
      dataPoints[i].update(xPos, yPos);
    } //for
    document.querySelector("#childOne").style.height = `${yPos + CELL_SIZE}px`;
  } //function

  /***********************************************/

  /******************* VISUALIZE THREE: Positive Mood Bubbles (Size-mapped) ******************/
  function visualizeThree(resJSON) {
    dataPoints = [];
    const container = document.querySelector("#childOne");
    container.innerHTML = "";
    const description = document.querySelector("#Ex4_title");
    description.textContent = "Positive Mood Balloons!";
    container.style.background = "rgba(255, 245, 200, 0.3)";

    const moodColors = {
      happy: "rgba(255, 223, 100,0.8)",
      neutral: "rgba(100, 200, 255,0.7)",
      calm: "rgba(150, 255, 180,0.7)",
      serene: "rgba(200, 250, 255,0.6)",
      well: "rgba(255, 200, 200,0.7)"
    };

    const results = resJSON.results;

    // Create balloon-like bubbles
    results.forEach(r => {
      const dp = new myDataPoint(
        r.dataId, r.day, r.weather, r.start_mood, r.after_mood,
        r.after_mood_strength, r.event_affect_strength, r.event_name,
        moodColors[r.after_mood] || "rgba(200,200,200,0.5)",
        container, "point_two"
      );

      // random starting position along the bottom
      dp.xPos = Math.random() * (window.innerWidth - 50);
      dp.yPos = 400 + Math.random() * 50;

      // random balloon size
      dp.size = 20 + Math.random() * 30;
      dp.update(dp.xPos, dp.yPos);

      // animation parameters
      dp.floatSpeed = 0.5 + Math.random() * 1;    // upward speed
      dp.swayAmplitude = 20 + Math.random() * 20; // side sway
      dp.swayOffset = Math.random() * Math.PI * 2;

      dataPoints.push(dp);
    });

    // Animate floating balloons
    if (window.visualInterval) clearInterval(window.visualInterval);
    window.visualInterval = setInterval(() => {
      dataPoints.forEach(dp => {
        dp.yPos -= dp.floatSpeed; // float upwards
        if (dp.yPos + dp.size < 0) dp.yPos = 450; // reset from bottom
        dp.xPos += Math.sin(Date.now() / 1000 + dp.swayOffset) * 0.5 * dp.swayAmplitude;
        dp.update(dp.xPos, dp.yPos);
      });
    }, 30);
  }

  /******************* VISUALIZE FOUR: floating hovering orbs ******************/
  function visualizeFour(resJSON) {
    dataPoints = [];
    const container = document.querySelector("#childOne");
    container.innerHTML = "";
    let description = document.querySelector("#Ex4_title");
    description.textContent = "Event Timeline by Mood";
    container.style.background = "rgba(220, 240, 255, 0.3)";

    const colors = {
      happy: "yellow",
      neutral: "lightblue",
      calm: "lightgreen",
      serene: "aqua",
      well: "pink",
      sad: "purple",
      angry: "red",
      anxious: "orange",
      moody: "grey",
      hurt: "brown"
    };

    const results = resJSON.results;

    // create event rows dynamically
    const eventNames = [...new Set(results.map(r => r.event_name))];
    let eventRows = {};
    let currentY = 50;
    const rowHeight = 40;
    eventNames.forEach(ev => {
      eventRows[ev] = currentY;
      currentY += rowHeight;
    });

    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    const xSpacing = 50;

    // store points for animation
    const points = [];

    results.forEach(r => {
      let dp = new myDataPoint(
        r.dataId, r.day, r.weather, r.start_mood, r.after_mood,
        r.after_mood_strength, r.event_affect_strength, r.event_name,
        colors[r.after_mood] || "gray",
        container, "point_two"
      );

      let xPos = xSpacing * (days.indexOf(r.day) + 1);
      let yPos = eventRows[r.event_name];
      dp.update(xPos, yPos);

      // save original positions for animation
      dp.origX = xPos;
      dp.origY = yPos;
      dp.offset = Math.random() * Math.PI * 2; // random phase for variation
      points.push(dp);
      dataPoints.push(dp);
    });

    // animate bouncing
    setInterval(() => {
      points.forEach(dp => {
        let bounce = Math.sin(Date.now() / 500 + dp.offset) * 5; // vertical bounce
        let sway = Math.cos(Date.now() / 700 + dp.offset) * 3;   // slight horizontal sway
        dp.update(dp.origX + sway, dp.origY + bounce);
      });
    }, 50);
  }


  /******************* VISUALIZE FIVE: Animated Bar Chart ******************/
  function visualizeFive(resJSON) {
    dataPoints = [];
    const container = document.querySelector("#childOne");
    container.innerHTML = "";
    let description = document.querySelector("#Ex4_title");
    description.textContent = "Floating Event Strength Orbs";
    container.style.background = "rgba(255, 230, 230, 0.3)";

    const colors = {
      happy: "yellow",
      neutral: "lightblue",
      calm: "lightgreen",
      serene: "aqua",
      well: "pink",
      sad: "purple",
      angry: "red",
      anxious: "orange",
      moody: "grey",
      hurt: "brown"
    };

    const results = resJSON.results;
    const points = [];

    results.forEach((r, i) => {
      let dp = new myDataPoint(
        r.dataId, r.day, r.weather, r.start_mood, r.after_mood,
        r.after_mood_strength, r.event_affect_strength, r.event_name,
        colors[r.after_mood] || "rgba(255,150,150,0.7)",
        container, "point_two"
      );

      dp.xPos = 50 + (i % 20) * 60;
      dp.yPos = 100 + Math.random() * 200;
      dp.origY = dp.yPos;
      dp.offset = Math.random() * Math.PI * 2;
      dp.update(dp.xPos, dp.yPos);

      points.push(dp);
      dataPoints.push(dp);
    });

    //animate floating up and down
    setInterval(() => {
      points.forEach(dp => {
        dp.yPos = dp.origY + Math.sin(Date.now() / 500 + dp.offset) * 20;
        dp.xPos += Math.cos(Date.now() / 700 + dp.offset) * 0.5;
        dp.update(dp.xPos, dp.yPos);
      });
    }, 50);
  }

  /******************* VISUALIZE SIX: Stormy Clouds ******************/
  function visualizeSix(resJSON) {
    dataPoints = [];
    const container = document.querySelector("#childOne");
    container.innerHTML = "";
    let description = document.querySelector("#Ex4_title");
    description.textContent = "Stormy Negative Moods by Weather";
    container.style.background = "rgba(200,200,255,0.2)";

    const results = resJSON.results;

    // extract unique weather types from results
    const weatherGroups = {};
    let currentX = 50;
    const yStart = 100;

    const uniqueWeather = [...new Set(results.map(r => r.weather))];
    uniqueWeather.forEach(w => {
      weatherGroups[w] = currentX;
      currentX += 120;
    });

    const colors = {
      sad: "purple",
      angry: "red",
      neutral: "gray",
      anxious: "orange",
      moody: "darkgrey",
      hurt: "brown"
    };

    results.forEach(r => {
      let dp = new myDataPoint(
        r.dataId, r.day, r.weather, r.start_mood, r.after_mood,
        r.after_mood_strength, r.event_affect_strength, r.event_name,
        colors[r.after_mood] || "grey",
        container, "point_two"
      );

      dp.xPos = weatherGroups[r.weather] + Math.random() * 50;
      dp.yPos = yStart + Math.random() * 200;
      dp.update(dp.xPos, dp.yPos);
      dataPoints.push(dp);
    });
  }

};
