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
Come On Down (Crystal Waters song): "Come On Down" is a 2001 single recorded by Crystal Waters, produced by Orlando Ortiz and co-written with Waters and Robert A. Israel.  The track, her first release for Strictly Rhythm Records, samples the theme song to the American game show "The Price Is Right", whose music was written and produced by Israel for his in-house company Score Productions.  The show's parent company Pearson Television (now part of FremantleMedia) gave its blessing to let Waters use the theme song, and as such received publishing rights and credits on the song.  The single also marked the first time that lyrics were added to "The Price Is Right" theme song and the first song based on a television theme song (and the first to come from a game show) to reach number 1 on the "Billboard" Hot Dance Club Play Chart the week of December 29, 2001.

KISZ-FM: KISZ-FM, 97.9 "Kiss Country," is a country music radio station in the Four Corners area of the Western United States.  It is licensed to Cortez, Colorado and is owned by Winton Road Broadcasting Company, LLC.  Bill Kruger-Regional Director, Don Kirk-Program Director.  Overnights feature "Kickin It With Kix", hosted by Kix Brooks.  Weekday mornings are hosted by nationally syndicated Big D, and Bubba.  Evenings feature Lia Night, and the award-winning "Nights with Lia" Monday through Saturday.  "Solid Gold Saturday Morning" airs 6-10am each Saturday morning.  Sunday's feature the "American Christian Music Review", Thunder Road", "American Country Countdown", and "The Road".

List of Rage of Bahamut episodes: Rage of Bahamut (神撃のバハムート , Shingeki no Bahamut ) is a Japanese anime television series produced by MAPPA that is based on the "Rage of Bahamut" game.  The anime aired between October 6, 2014 and December 29, 2014 for 12 episodes.  On May 6, 2015, a second season was announced at the series' orchestra concert event.  Titled Rage of Bahamut: Virgin Soul (神撃のバハムート VIRGIN SOUL , Shingeki no Bahamut: Virgin Soul ) , it premiered on April 7, 2017.  The opening theme song "EXiSTENCE" is performed by SiM, while the ending theme song "Promised Land" is performed by Risa Shimizu.  For season 2, the first opening theme song is "LET iT END" by SiM while the first ending theme song is "Haikei Goodbye Sayonara" (拝啓グッバイさようなら , lit.  Greetings, Goodbye, Farewell) by DAOKO.  The second opening theme is "Walk This Way" by THE BEAT GARDEN, while the second ending theme is "Cinderella Step" by DAOKO.

Thunder Road (film): Thunder Road is a black and white 1958 drama–crime film about running moonshine in the mountains of Kentucky and Tennessee in the late 1950s.  It was directed by Arthur Ripley and starred Robert Mitchum, who also produced the film, co-wrote the screenplay, and is rumored to have directed much of the film himself.  He also co-wrote (with Don Raye) the theme song, "The Ballad of Thunder Road".

Moonrunners: Moonrunners is a 1975 film, starring James Mitchum, about a Southern family that runs bootleg liquor.  It was reworked four years later into the popular long-running television series "The Dukes of Hazzard", and as such the two productions share many similar concepts.  Mitchum had co-starred with his father, Robert Mitchum, in the similar drive-in favorite "Thunder Road" eighteen years earlier, which also focused upon moonshine-running bootleggers using fast cars to elude federal agents.  "Moonrunners", a B movie, was filmed in 1973 and awaited release for over a year.  Its soundtrack reflects the outlaw music boom of the 1970s during which the film was released.

Thunder Road (roller coaster): Thunder Road was a wooden roller coaster located at Carowinds amusement park on the border between Fort Mill, South Carolina, and Charlotte, North Carolina.  Opened in 1976 and built by Philadelphia Toboggan Coasters, the racing roller coaster cost $1.6 million to construct and featured two identical tracks that paralleled each other.  The design of the ride was based on Rebel Yell, a wooden racing coaster at Kings Dominion in Doswell, Virginia.  Thunder Road was closed on July 26, 2015, to make room for expansion at the park.  On August 27, 2015, Carowinds announced that the Boomerang Bay waterpark would be expanded and renamed Carolina Harbor.  The expansion resulted in the removal of Thunder Road.

Thunder Road International SpeedBowl: Thunder Road International SpeedBowl, more commonly known as Thunder Road, is a .25 mi high-banked, paved short track speedway located in the town of Barre, Vermont, just outside the limits of the city of Barre.  The track was founded by Ken Squier and Tom Curley in 1960 and sold in the spring of 2017 to former Thunder Road track champion Cris Michaud and local businessman Pat Malone.  Currently, Thunder Road hosts three weekly divisions: Late Models, Tiger Sportsman and Street Stocks.  The track is known for hosting its weekly races on Thursday night, rather than Saturday, as nearly all other short tracks do.  On June 28, 2007, NASCAR driver Kenny Wallace raced at Thunder Road.  Ken Schrader, another NASCAR driver, had raced once at Thunder Road each of the two years prior to Wallace's visit.

Charlotte Marathon: The Novant Health Charlotte Marathon is an annual marathon which takes place in Charlotte, North Carolina, every November.  It was previously called Thunder Road Marathon and used to feature a NASCAR theme in keeping with the region's close ties to auto racing.

The Ballad of Thunder Road: "The Ballad of Thunder Road" is a song performed and co-written by actor Robert Mitchum in 1957, with music by composer Jack Marshall.  It was the theme song of the movie "Thunder Road".  The song made the Billboard Hot 100 twice, in 1958 and 1962, and while it never peaked higher than #62, it racked up 21 total weeks in the chart.  The song moves ominously between minor and major keys.

Florida State Road 136: State Road 136 (SR 136), locally known as Thunder Road, is a 3.396 mi east–west route in Suwannee, Columbia and Hamilton Counties.  Its western terminus is just west of Interstate 75 and is a continuation of County Road 136 in rural Suwannee County.  Its eastern terminus is US 41 in White Springs.

Question: What Moonrunners father co-wrote the theme song to Thunder Road?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "moonrunners_actor": {
      "type": "string",
      "description": "The actor who starred in the film Moonrunners."
    },
    "actor_father": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor's father."
        },
        "role_in_theme_song": {
          "type": "string",
          "description": "The role the father played in the theme song's creation."
        }
      },
      "required": [
        "name",
        "role_in_theme_song"
      ],
      "additionalProperties": false
    },
    "theme_song_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the theme song."
        },
        "film_associated_with": {
          "type": "string",
          "description": "The film the theme song is associated with."
        }
      },
      "required": [
        "title",
        "film_associated_with"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "moonrunners_actor",
    "actor_father",
    "theme_song_details"
  ],
  "additionalProperties": false
}
