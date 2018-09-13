---
layout: post
published: true
title: First step towards AI - Hard Coding!
subtitle: Hard Coding an Automated Shower
gh-repo: syeddanish41/know-it-all-shower
gh-badge:
  - star
  - watch
  - follow
tags:
  - Projects
  - Automation
---
The term Artificial Intelligence has been around for more than half a century - it started out with a simple idea of automating the tasks requiring human intervention. It is the innate property of laziness(& innovation 😅) in humans that gave rise to this Idea - extending ourselves with intelligent "modules," which makes our lives easier/better.

I started out on the journey of AI following the same idea - automating the simple tasks - to skip one mundane step in daily life. During my second year vacations from college, I was into robotics, and I was building standard examples such as [line follower](https://www.youtube.com/watch?v=JDxIorDI1VQ), [self-balancer](https://www.youtube.com/watch?v=_afq1DTAJZo) and [object follower](https://www.youtube.com/watch?v=lsEr7UbAK5A), all Arduino based designs. It wasn’t very satisfying because I was writing code but not solving problems. One day, when I was taking a shower(an activity where you get the best ideas) it struck me, Why not make the shower smarter? It was then, all the **‘how’** questions popped up in my head, and my inquisitive brain started churning out fast answers. :

- How to detect human presence? - Ultrasound sensor
- How to operate the shower knobs? - DC Motors
- Well, How to coordinate different components? - Duh.. you already have an Arduino
- It would be fancy if I could control the temperature? - Yes!
- Dude, that’s genius, but how? – Hard code it.
- Can I name it Jarvis? - Eh, **Know-it-all Shower** is better.

        
### Know-it-all Shower
The shower was fitted with ultrasound sensors to detect human presence. DC motors, clamped onto the shower knobs using metal contraptions, were operating the structure as they detect the human presence. The water temperature control was implemented by **“hard coding”** the logic - for cold weather turn left knob(cold water) by x degrees and right knob(hot water) by x + Δx and vice versa for warm weather.

Simple, right?

What started out as a fun project years ago, led me to research into the practical applications of AI over all these years. This experience made me realize that the central aspect is identifying the right problems. 
Since then, I have been exploring the idea of replacing the “Hard Coded” temperature detector with a Reinforcement Learning algorithm that makes it an inch closer to **today’s AI**.


**PS:** This novice experiment bagged the third prize on Instructables in Home Automation category. 
If that seemed exciting to you, a detailed publication on Know-it-all Shower could be found on Instructables website - [here](https://www.instructables.com/id/The-know-it-all-Shower/).

Code repository can be found on my Github page - [here](https://github.com/syeddanish41/know-it-all-shower).
