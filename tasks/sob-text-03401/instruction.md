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
The Spirit of '43: The Spirit of '43 is an American animated World War II propaganda film created by Walt Disney Studios in 1943 and released in January 1943.  The film stars Donald Duck, and arguably contains the first appearance of a prototype for the character Scrooge McDuck, not named in the film.  It is a sequel to "The New Spirit".  The purpose of the film is to encourage patriotic Americans to file and pay their income taxes faithfully in order to help the war effort.  The repeated theme in the film is "Taxes... To Defeat the Axis."

DuckTales (video game): DuckTales (わんぱくダック夢冒険 , Wanpaku Dakku Yume Bōken , lit.  "Naughty Ducks Dream Adventures") is an action platformer video game developed and published by Capcom and based on the Disney animated TV series of the same name.  It was first released in North America for the Nintendo Entertainment System in 1989 and was later ported to the Game Boy in 1990.  The story involves Scrooge McDuck traveling around the globe collecting treasure and outwitting his rival Flintheart Glomgold to become the world's richest duck.

Sacco van der Made: Gerard Johannes "Sacco" van der Made (4 April 1918, Rotterdam – 21 December 1997, Rotterdam) was a Dutch actor and voice actor.  He provided the voice of Scrooge McDuck in the Dutch version in the television show "DuckTales".  His last big TV role was that of Bert Jansen in the comedy show "Het zonnetje in huis", the Dutch version of "Tom, Dick and Harriet".  His last role was that of Gerard Krol in the crime series "Baantjer".  He died at the age of 79 and is buried at a general burial site in Nisse.

DuckTales (2017 TV series): DuckTales is an American animated television series developed by Matt Youngberg and Francisco Angones for Disney XD.  Produced by Disney Television Animation, the series is a reboot of the original 1987 series of the same name.  "DuckTales" was announced in February 2015 and premiered on August 12, 2017 with a 44 minute special entitled "Woo-oo!" .  The first season, which resumed on September 23, 2017, will consist of 21 twenty two minute episodes and an additional 44 minute special.  The series was renewed for a second season on March 2, 2017.

Alan Young: Alan Young (born Angus Young; November 19, 1919 – May 19, 2016) was a British-born Canadian-American actor, voice actor, comedian and radio and television host/personality who "TV Guide" called "The Charlie Chaplin of Television".  He was best known for his role as naive Wilbur Post in the television comedy series "Mister Ed" (1961–1966).  Young was also the voice of Disney's Scrooge McDuck for over thirty years, first in the Academy Award-nominated short film "Mickey's Christmas Carol" (1983) and in various other films, TV series and video games until his death.  During the 1940s and 1950s, he starred in his own variety/comedy sketch shows "The Alan Young Show" on radio and television, the latter gaining him two Emmy Awards in 1951.  He also appeared in a number of feature films, starting from 1946, including the 1960 film "The Time Machine" and from the 1980s gaining a new generation of viewers appearing in numerous Walt Disney Productions films as both an actor and voice actor.

List of DuckTales episodes: The following is an episode list for the Disney animated television series "DuckTales".  The series is based on the Scrooge McDuck character and the "Uncle Scrooge" comic books created by Carl Barks.  The series stars Scrooge, his grand nephews Huey, Dewey, and Louie and Webby Vanderquack, and several new characters created explicitly for the series.  While Huey, Dewey, and Louie originated in Donald Duck animated short subjects in the 1930s, their characterization on "DuckTales" approximated that of Barks' comics.  Although Donald Duck was a major player in the "Uncle Scrooge" comics, he only appeared as a guest star in a few "DuckTales" episodes.

David Tennant: David Tennant (born David John McDonald; 18 April 1971) is a Scottish actor and voice actor.  He is best known for his roles as the Tenth Doctor in the British television series "Doctor Who", Alec Hardy in "Broadchurch", Giacomo Casanova in the TV serial "Casanova", Kilgrave in "Jessica Jones", and Barty Crouch, Jr.  in the film "Harry Potter and the Goblet of Fire".  In addition to his appearances on screen, he has worked as a voice actor and in theatre, including Prince Hamlet in a critically acclaimed 2008 stage production of "Hamlet" and as the voice of Scrooge McDuck in the new "DuckTales" series starting in 2017.  In January 2015, Tennant received the National Television Award for Special Recognition.

The Buckaroo of the Badlands: The Buckaroo of the Badlands is a Scrooge McDuck comic by Don Rosa.  It is the third of the original 12 chapters in the series The Life and Times of Scrooge McDuck.  The story takes place in 1882.  Fifteen-year-old Scrooge is traveling to the American West by train.  During a conversation with a man who owns some square eggs the train is robbed by Jesse James and his gang.  Scrooge fights them, but falls off the train himself.  He comes across some cowboys led by Murdo MacKenzie, transporting cattle and joins them, receiving his own horse, which he names after his sister Hortense, since they have the same bad temper.

Mickey's Christmas Carol: Mickey's Christmas Carol is a 1983 American animated featurette produced by Walt Disney Productions and released by Buena Vista Distribution.  It was directed and produced by Burny Mattinson.  The cartoon is an adaptation of Charles Dickens' "A Christmas Carol", starring Scrooge McDuck as Ebenezer Scrooge.  Many other Disney characters, primarily from the Mickey Mouse universe, "Robin Hood", and "The Adventures of Ichabod and Mr. Toad", were cast throughout the film.

DuckTales: DuckTales is an American animated television series, produced by Walt Disney Television Animation and Tokyo Movie Shinsha, and distributed by Buena Vista Television.  The cartoon series premiered on September 18, 1987, and ran for a total of 100 episodes over four seasons, with it final episode airing on November 28, 1990.  Based upon "Uncle Scrooge" and other Duck universe comic books created by Carl Barks, the show follows Scrooge McDuck, his three grandnephews Huey, Dewey, and Louie, and close friends of the group, on various adventures, most of which either involve seeking out treasure or thwarting the efforts of villains seeking to steal Scrooge's fortune or his Number One Dime.

Question: David Tennant was the voice of Scrooge McDuck in an American animated television series that was developed by Matt Youngberg and who else?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the animated television series."
    },
    "series_type": {
      "type": "string",
      "description": "The type of the series, e.g., animated television series."
    },
    "developer_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the individuals who developed the series."
    },
    "scrooge_mcduck_voice_actor": {
      "type": "string",
      "description": "The name of the voice actor for Scrooge McDuck in this series."
    }
  },
  "required": [
    "series_title",
    "series_type",
    "developer_names",
    "scrooge_mcduck_voice_actor"
  ],
  "additionalProperties": false
}
