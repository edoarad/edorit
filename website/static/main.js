// Including to, so that random(1, 3) returns one of 1,2,3.
function random(from, to) {
    return from + Math.floor(Math.random() * (to - from + 1));
}

function p(t) {
    return Math.random() < t;
}

// Bar.
$(function() {
    let $main = $("#main"), main = $main[0];

    let drinkLevel = 0;

    function animationStr(anim, time) {
        return anim + " " + time + "ms";
    }

    function animate() {
        let anim = [];
        let maxTime = 0;

        let log = Math.log2(drinkLevel) + 1;

        if (p(0.5)) {
            let rotSide = Math.random() < 0.5 ? "l" : "r";
            let time = random(800, 1800 * log);
            maxTime = Math.max(maxTime, time);
            anim.push(animationStr(rotSide + "rot-anim", time));
        }
        
        if (p(0.5)) {
            let time = random(800, 2200 * log);
            maxTime = Math.max(maxTime, time);
            anim.push(animationStr("skew-anim", time));
        }

        if (p(0.65)) {
            let time = random(800, 4000 * log);
            maxTime = Math.max(maxTime, time);
            anim.push(animationStr("blur-anim", time));
        }

        $main.css("animation", "");
        void main.offsetWidth; // This causes repainting, thus removing the previous animation.
        $main.css("animation", anim.join(", "));

        let delay = random(2000 / log, 10000 / log);

        setTimeout(animate, delay + maxTime);
    }

    $("#drink").click(function() {
        drinkLevel++;
        console.log("Drink level is now " + drinkLevel);
        if (drinkLevel === 1) {
            animate();
        }
    });
});