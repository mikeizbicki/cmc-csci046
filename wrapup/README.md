# Wrapup

<img src=733evqt0w4y41.jpg width=500px />

## Big ideas

1. For every data structure, know the runtimes of the operations
    1. Changing data structure (e.g. list -> deque, list -> numpy.array) can speed up the program dramatically
        1. "No free lunch": there is no universally optimal data structure
    1. Quadratic runtimes are the worst
        1. Fast enough that you don't notice a problem at first
        1. But once there's lots of data, things get REAL SLOW
        1. Happens all the time in practice:

           1. Microsoft Windows arranging the tiles on the desktop

              https://randomascii.wordpress.com/2021/02/16/arranging-invisible-icons-in-quadratic-time/
        
           1. reduce GTA load times from 7 minutes to instant by removing accidentally quadratic code

              https://nee.lv/2021/02/28/How-I-cut-GTA-Online-loading-times-by-70/

           1. stackoverflow crashed due to accidentally quadratic code
           
              https://stackstatus.net/post/147710624694/outage-postmortem-july-20-2016

           1. many more examples
           
              https://accidentallyquadratic.tumblr.com/

1. Binary Search/AVL tree is magical
    1. O(n) => O(log n) = basically instant for all n
    1. Foundational data structure for all CS applications

1. Big-O/Omega/Theta are general purpose mathematical functions, and not specific to runtimes

   <img src=t32o3zhn1e461.jpg width=600px />

1. We covered lots of material not "traditionally" taught in data structures

   Focus on real-world program development

    1. git
    1. test driven development (+ continuous integration)
    1. creating/publishing python libraries
    1. open source
    1. MapReduce
    1. bash scripting
    1. unicode and non-English languages

1. We didn't cover
    1. memory management details
    1. python is a "garbage collected" language, so these details are handled automatically
    1. other classes taught in C/C++ need to manage these details
    1. data scientists don't need to care about these details

1. Good tools make you more efficient
    1. Use linux:
        1. Even Microsoft uses more Linux than Windows

           https://www.zdnet.com/article/microsoft-developer-reveals-linux-is-now-more-used-on-azure-than-windows-server/

        1. <img src=y9nmw0smgxd61.png width=400px/>
    1. Use:
        1. a good text editor (e.g. vim)
        1. version control (e.g. git)
        1. good test cases, continuous integration whenever possible (e.g. github actions)

           <img src=Strips-Test-audimetre-600-finalenglish.jpg width=500px />

Where to go from here?
1. CSCI143: Big Data (practice of data science)
1. CSCI145/MATH166: Data Mining (theory of data science)
1. CSCI148: Graph Algorithms (SWE interview questions)

**If there's ever anything I can do to help you in the future, please reach out.**

1. advice on classes
1. advice on how to implement a project
1. get involved with research
1. etc.

## Final

1. 40 points

   (currently about 200 points in the class => 20% of grade)

1. I'll post it Monday, you'll have until Sunday

1. Follow the same format as the practice exam

## Course evals

Please complete the course eval

