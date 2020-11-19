// File declaration


//Logic
/*
When page loads:
X number of images selected from a pool of images
Images associated to a random index value between 0 and X
Images aligned in an array in order of index values
SPIN button is clicked
Random number is generated as winner, which will be associated to the index value
Images animate 'spinning' left off screen, wrapping to the other side and back to start 
(wrapping could be a trick of doubling the array of images which trail offscreen, then jump to start position when last image finishes the animation)
Animation repeats 3 times, with 3rd animation at a slower speed
3rd animation comes to a complete stop when winning image index is center screen and all images retain their current position.
(if the above is not possible, I can generate the array of images with the winning image always in the middle, however that means clever people will catch on that they win whichever image is started on)



Winning prize should be determined by a generated MD5 hash, next player to open a box will win that predetermined hash. This is for security and fairness.
*/

