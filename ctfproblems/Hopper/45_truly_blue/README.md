# Last Bit Steganography

The contestant is given an image, told that it is nothing more than the Andover blue! This is of
course a lie: it's close, but a message has been hidden using last bit steganography.

First, the contestant needs to read in the pixel data fron the PNG. The color itself is the one that
shows up in the header of the Andover website, but you don't even need that information: you can
simply notice that the image is *almost* monochromatic, down to the last bit of each RGB pixel
value. The data is encoded in UTF-8, in the last bit of each pixel color, in the order r1, g1, b1,
r2, g2, b2, etc., proceeding top-down and left-right. (From a problem design perspective, this is
the weakest part of the problem: it's not immediately obvious that this is the encoding, and one
could conceivably abandon this line of thinking after trying a different ordering.)

Reading in the last bit of each pixel will produce a message with lots of filler text (mainly so
that more pixels would differ from the base) and text giving the flag. The `encoder.py` script
provides a decoding function, and shows how a decoding function given only the pixel data retrieves
the original message, complete with flag. The flag itself can be anything.

## Commentary

I've never actually seen a steg problem do this, even though it's a really common steg technique. The idea is just that the last bit of RGB colors doesn't mean much, so changing them allows you to store data without being detected.

I was originally thinking of making this a lot harder: an image that I took personally and so can't be clearly identified as using last-bit steg, or a famous image that you'd have to think to download again and compare or something like that, along with being a lot more cryptic about the clues. I see this more as an easy-mid problem than as a hard one: if you're familiar with last-bit steg this should be easy, if you aren't there's hopefully an "aha, clever" moment when you open GIMP or something and see that the colors are all slightly different from each other. The hints are pretty nice: to be honest you're halfway there once you open it in an image editor that shows you hex values.

As far as design, the main issue is that it's unclear in what order you read pixels. I hope the one
I use is the first one most people would think of: it'd suck to write one that checked each channel
in order or something like that. Hopefully it's pretty obvious to try encoding it as ASCII before
trying a bitmap image or something else. I tried to look for online tools to do this, and I could
find a ton that used a similar method but nothing that would solve this exact problem: you'll
probably have to write some code. I wrote a function that solves it given the pixel data, which is a
one-line call from the PIL library. You need pillow to run it.

The other thing is the snarkiness of the problem text. It seems in line with previous PACTFs and the
general spirit of such competitions, but if it's laid on a bit too thick it can change.

## Flag
As of now, the flag is `last bits matter`.
