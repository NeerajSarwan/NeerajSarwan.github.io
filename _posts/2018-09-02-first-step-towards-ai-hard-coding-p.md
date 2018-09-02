---
layout: post
published: false
title: First step towards AI - Hard Coding!
subtitle: Hard Coding an Automated Shower
---
The term Artificial Intelligence has been around for more than half a century - it started out with a simple idea of automating the tasks requiring human intervention. It is the innate nature of laziness(& innovation 😅) in humans that gave rise to the Idea of Artificial Intelligence - to extend ourselves with intelligent "modules" which makes our lives easier/better.

I started out on the journey of AI following the same idea - automating a simple task - to skip one step in my daily life. During my second year vacations from college, I was into robotics and I was building standard examples such as [line follower](https://www.youtube.com/watch?v=JDxIorDI1VQ), [self balancer](https://www.youtube.com/watch?v=_afq1DTAJZo) and [object follower](https://www.youtube.com/watch?v=lsEr7UbAK5A), all arduino based designs. It wasn't very satisfying because I was not building any "solution". One day, when I was taking a bath(best place to get new ideas), it struck me - Why not automate the shower? It was then, all the questions popped along with the answers:
1. How to detect human presence? - Ultrasond sensor
2. How to open the shower knobs? - DC Motors
3. Control them? Duh.. you already have an Arduino 
4. Can I control the temperature? - Yes!
5. How? - **Hard Code it!**
6. Lastly, what should I name it? -

### Know-it-all Shower
Fitted with ultrasound sensors to detect human presence, dc motors are fitted on the shower knobs using metal contraptions, to operate when triggered. The water temperature control is implemented by "hard coding" the logic - for mild cold weather turn left knob(cold water) by x degrees and right knob(hot water) by x + Δx and vice versa for hot weather.
Simple, right?

What started out as a fun project, it led me to research into the practical applications of AI over the years. This experienc  made me realize. After 4 years, I have been thinking about revisiting the idea and replace the "Hard Coded" part with a Reinforcement Learning algorithm to train to make it more AI like.

PS : I won the third prize on Instructables in Home Automation Contest for this project. More detailed publication on know-it-all shower can be found [here](https://www.instructables.com/id/The-know-it-all-Shower/).

Code [here](https://github.com/syeddanish41/know-it-all-shower).





