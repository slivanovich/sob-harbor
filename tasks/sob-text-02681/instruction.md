Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Dan Peters: Daniel Joe Peters (born August 18, 1968) is the drummer for Mudhoney.  He joined Bundle of Hiss when he was fifteen years old.  He also played drums for Nirvana, appearing on one single, "Sliver".  Peters' only live appearance with Nirvana was on September 22, 1990, in Seattle, Washington, at the Motor Sports International Garage.  Peters continues to drum for Mudhoney, and was replaced in Nirvana by Dave Grohl.  Peters expressed his only regret as missing the chance to play drums on "Nevermind".  He returned to Mudhoney for the recording of "Every Good Boy Deserves Fudge".  He has stayed with Mudhoney ever since.  Mudhoney's latest offering is "Vanishing Point" released April 2, 2013.  Peters has also played drums for Ellensburg, Washington based band Screaming Trees from 1990 to 1991.  He also appeared in Black Sheep alongside David Spade and Chris Farley.  He is married to a prominent litigator with the Seattle-based, Emerald Law Group.  She was formerly a partner with the venerable law firm, Scott, Kinney & Mack pllc.

UFO (band): UFO are an English rock band that was formed in London in 1969.  They became a transitional group between early hard rock and heavy metal and the new wave of British heavy metal.  The band's current lineup includes vocalist Phil Mogg, guitarist Vinnie Moore, bass guitarist Rob De Luca, keyboardist and rhythm guitarist Paul Raymond and drummer Andy Parker.  They have gone through several line-up changes, leaving Mogg as the only constant member, and had two hiatuses (1983–1984 and again from 1989 to 1991).  The band are also notable for featuring former Scorpions guitarist and MSG founder Michael Schenker, who was a member of UFO from 1973 to 1978 and again, occasionally, between 1993 and 2003, when Moore replaced him.

Legends of Rock at Castle Donington: Legends of Rock: Live at Castle Donington is a DVD released by German guitarist Uli Jon Roth.  It features Roth's headlining show at Castle Donington, Leicestershire, England in 2001, along with his special guests Michael Schenker, Phil Mogg, and Pete Way from UFO, and Jack Bruce from Cream.  Released in 2002.

Misdemeanor (UFO album): Misdemeanor is the twelfth studio album by the British hard rock band UFO.  After the disastrous tour supporting "Making Contact", UFO disbanded, with Phil Mogg spending time in Los Angeles, where he contacted (through Mike Varney) guitarist Atomik Tommy M.  Mogg decided to start a new band, involving the new American guitarist and Paul Gray, who had played bass guitar in the last UFO tour.  The three of them recruited former UFO keyboard player Paul Raymond and drummer Robbie France and started writing new material.  Chrysalis Records signed the new band as UFO and assigned experienced producer Nick Tauber for the recording process of a new album.  France resigned before the recording started and was replaced by former Magnum drummer Jim Simpson.  Paul Raymond quit the band during their US tour in August 1986 and was replaced for the rest of the tour by David Jacobson.

Dave Peters: Dave Peters is an American musician.  He was the original guitarist for the band Eighteen Visions, guitarist for the band Throwdown, and, as of 2002, the vocalist for Throwdown.  He did guest vocals for the song "Unleash" by groove metal band Soulfly, for the song "Feel as Though You Could" by Demon Hunter, and the song "Despair" for Living Sacrifice.  He is straight edge.

Unleash (song): "Unleash" is a Soulfly song, released from the 2008 album "Conquer".  This single, along with music video, was released a month before the album's release and was the album's first of two singles.  Dave Peters (member of Throwdown) is the guest vocalist, and helped Max Cavalera write lyrics prior to the recording.

Phil Mogg: Phillip John Mogg (born 15 April 1948, Wood Green, North London) is the lead singer for the English rock band UFO, which he formed with longtime friends Pete Way and Andy Parker.  Mogg wrote the majority of the band's lyrics, with the music being written by Way, Michael Schenker, and later, Paul Raymond, but Schenker left to launch his solo career in 1979.  Beginning in 1997, Mogg and Way, under the moniker Mogg/Way, released a couple of albums- "Edge of the World" and "Chocolate Box".  With UFO on hiatus, Phil formed another side project, $ign of 4.  In late 2003, having regained the rights to the UFO name from Schenker, Mogg spoke with Pete Way and Paul Raymond, and ended up having a reunion tour which later brought the band back for good, with newly hired American guitarist Vinnie Moore.  The band then released several new albums : "Showtime", "You Are Here", "The Monkey Puzzle", "The Visitor", "Seven Deadly" and "A Conspiracy of Stars".

The Plot (band): The Plot was a heavy rock band formed in 2003 by bassist Pete Way and his long-time friend, guitarist Michael Schenker.  The two wanted to form a band like UFO again and asked Phil Mogg and Andy Parker to regroup with them, but tension was still fiery between the ex-bandmates, although Way, Schenker and Mogg had been involved in recording as UFO for the album "Sharks" in 2002.  So instead, Way and Schenker recruited drummer Jeff Martin.  This band released one album, also entitled "The Plot".

Die' Hunns: Die Hunns (originally known as Duane Peters and the Hunns) is an American punk rock band formed in 2000 by front-man Duane Peters, of US Bombs fame.  The band has featured a rotating cast of musicians with Peters as the only constant.  In 2002 Peters met Corey Parks (sister of former NBA basketball player Cherokee Parks), formerly of Nashville Pussy, at The Damned show.  Parks would later marry Peters and join the band as both a vocalist and bassist.

Let It Rock (magazine): Let It Rock was a monthly British music magazine, which featured lengthy critical articles, record reviews, and feature articles covering a wide spectrum of popular music, including soul, reggae, and blues.  Between October 1972 and December 1975, 35 issues of the magazine were published in London.  Dave Laing was the founding editor; John Pidgeon took over as editor in October 1973.  The reviews editor was Simon Frith, and Charlie Gillett was consultant editor.  Other contributors included John Peel, Lester Bangs, Michael Gray, Mick Gold, Mick Houghton, Jean Peters, David Downing, Gary Herman, Idris Walters, Karl Dallas and Phil Hardy, and the soul music column was written by Pete Wingfield.  Designers and illustrators included Barney Bubbles, George Snow, Kevin Sparrow and Peter Till.  The magazine struggled to achieve consistent sales of 20,000 and closed due to market forces.  Music writers David Hepworth and Barney Hoskyns have called "Let It Rock" influential, and suggested that it was the precursor of such music publications as "Q magazine" and "Mojo".

Question:  Are Phil Mogg and Dave Peters musicians?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_musicians": {
      "type": "boolean",
      "description": "True if both Phil Mogg and Dave Peters are identified as musicians."
    },
    "musician_count": {
      "type": "integer",
      "description": "The number of individuals from the question who are identified as musicians."
    },
    "individuals_details": {
      "type": "array",
      "description": "Details for each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_musician": {
            "type": "boolean",
            "description": "True if the individual is identified as a musician."
          },
          "musical_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The musical roles of the individual, if they are a musician."
          },
          "bands_involved_with": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The bands or projects the individual has been involved with, if they are a musician."
          }
        },
        "required": [
          "name",
          "is_musician"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "are_both_musicians",
    "musician_count",
    "individuals_details"
  ],
  "additionalProperties": false
}
