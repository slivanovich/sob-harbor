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
Jonathan Davis and the SFA: Jonathan Davis and the SFA (Simply Fucking Amazings) is the solo band of Korn frontman Jonathan Davis.

Rich Versus Roach: Rich versus Roach is a 1959 studio album by drummers Buddy Rich and Max Roach with their respective bands of the time.  The album is mixed with each of the two bands in a different stereo channel.

Faget (song): "Faget" is a song by the American nu metal band Korn.  It is the sixth track from the band's self-titled debut studio album.  The song is about how Korn's lead vocalist Jonathan Davis was bullied in high school for being into arts, wearing eyeliner, being into new wave music (for example, Duran Duran), and wearing frilly shirts.  According to Jonathan Davis, he was constantly called names such as "faggot".  Also, there was a rumor that Davis was gay.  Jonathan Davis said he did not know if he was gay or not.  Therefore, Davis tried to get in a relationship with another boy.  However, Jonathan Davis disliked the experience, realizing he is not gay, even if people thought he was.

Stephen Christian: Stephen Christian is an American singer and songwriter best known as the former lead vocalist of the alternative rock band Anberlin, as well as the vocalist of his acoustic side-project Anchor & Braille.  He and his bandmates started Anberlin in 2002, after the demise of their previous group, known as SaGoh 24/7.  He is one of the main songwriters for Anberlin along with Joseph Milligan, and with the band has released seven albums, the final being in 2014.  Many of the albums in the Anberlin discography have peaked in the top ten on various "Billboard" charts.

Anchor &amp; Braille: Anchor & Braille is the recording alias for American singer and songwriter Stephen Christian, known for fronting the alternative rock band Anberlin, before its dissolution in 2014.  Originally conceived as a side project for Christian, Anchor & Braille is now his primary vehicle for releasing music.  Christian has described Anchor & Braille as a collaborative effort, having recorded with musicians such as Aaron Marsh of Copeland, Micah Tawlks, and Kevin Daily of Civil Twilight.  Since its beginning, Christian has released three studio albums under this name, Felt in 2009, The Quiet Life in 2012, and Songs for the Late Night Drive Home in 2016.

Alone I Play: Alone I Play is a special limited run DVD/CD combo set by Korn vocalist Jonathan Davis, which was released November 10, 2007 on "Invisible Arts".  The album was recorded and videotaped at Malibu's Woodshed Recorder on November 7, 2007, the day before Davis embarked on his first solo tour, the Alone I Play tour.  "Alone I Play" was recorded and packaged in CD and DVD formats and prepared for sale in no longer than three days, where it is sold at venues where Davis performs (although a commercial release is planned).  The album features songs originally composed by Davis and Gibbs for the 2002 film "Queen of the Damned", as well as classic and uncommonly performed Korn songs.  Despite the fact that this is a solo effort, three members of Korn's backup band appear on "Alone I Play": keyboardist Zac Baird, guitarist Shane Gibson and percussionist Michael Jochum.  The renowned and eclectic Indian violinist and composer L. Shankar, also known as Shenkar, also makes an appearance.  The album's title is a pun on Korn's 2002 single "Alone I Break".

Jonathan Davis: Jonathan Howsmon Davis (born January 18, 1971), also known as JD and JDevil (or J Devil), is an American musician best known as the leading vocalist and frontman of the nu metal band Korn.

New Waves: New Waves is the tenth studio album by American hip hop group Bone Thugs-n-Harmony.  It was released on June 23, 2017, by Entertainment One Music.  The album only consists of 2 out of 5 members of Bone Thugs-n-Harmony (Krayzie Bone and Bizzy Bone; a duo simply known as "Bone Thugs").  The album features a large selection of guest appearances, including Stephen Marley, Tank, Jesse Rankins, Kaci Brown, Jazze Pha, the other Bone members (Layzie Bone, Wish Bone and Flesh-n-Bone), Jonathan Davis from nu metal band Korn, Bun B, Uncle Murda, Yelawolf, IYAZ, Eric Bellinger and more.

Pretendo: Pretendo is a New York City-based indie rock band formed in 2004 of ex-/present members of Enon, Skeleton Key, Creedle, The Rugburns, Mono Puff, Morricone Youth, Little Jack Melody and The DaoSon For.  Guitarist/vocalist Devon E. Levins and bassist/vocalist John Castro were childhood friends playing in the Las Vegas hardcore punk band Abeyance in the 1980s.  E. Levins met drummer Stephen Calhoon in 1997 when their respective bands Creedle and Skeleton Key had played together.  Pretendo recorded its debut eponymous album with Wharton Tiers in New York City at Fun City Studio, which was released on April 5, 2005 by Country Club Records.  Pretendo's second album entitled "][" (or "Two") was recorded in 2007 by Martin Bisi at B.C. Studio in Brooklyn, New York and includes artwork and lyrics contributed by contemporary pop artist Ron English. "] [" was released on March 4, 2008 by Country Club Records.  The band has commenced work on its third album, tentatively entitled "]|[", with new members Kenny Shaw replacing Stephen Calhoon on drums and Dan Kessler on keyboards.

Army of Anyone: Army of Anyone was a rock supergroup formed by Filter frontman Richard Patrick with two members of rock band Stone Temple Pilots.  In addition to Patrick on vocals, the band featured brothers Dean DeLeo and Robert DeLeo on guitar and bass respectively, and Ray Luzier, formerly of David Lee Roth's band, on drums.  The band released one self-titled album in November 2006, which was well-received, but sold well short of the member's multi-platinum selling releases of their other bands.  After touring in support of the album, the band went into hiatus in mid-2007, with members returning to their respective bands, except Luzier, who joined Korn.  Despite being relatively inactive since 2007, all members have stayed in contact, and have independently shown interest in working on a second album if the logistics and scheduling of their commitments to other bands ever aligned.

Question: What role in their respective bands do Stephen Christian and Jonathan Davis share?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shared_role": {
      "type": "string",
      "description": "The common role shared by the musicians."
    },
    "musicians": {
      "type": "array",
      "description": "List of musicians and their primary bands.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the musician."
          },
          "band": {
            "type": "string",
            "description": "The primary band of the musician."
          }
        },
        "required": [
          "name",
          "band"
        ],
        "additionalProperties": false
      }
    },
    "role_description": {
      "type": "string",
      "description": "A brief description of the shared role."
    }
  },
  "required": [
    "shared_role",
    "musicians",
    "role_description"
  ],
  "additionalProperties": false
}
