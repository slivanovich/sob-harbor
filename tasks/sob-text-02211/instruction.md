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
Have I the Right?: "Have I the Right?"  was the début single and biggest hit of British band The Honeycombs.  It was composed by Ken Howard and Alan Blaikley, who had made contact with The Honeycombs, a London-based group, then playing under the name of The Sheratons, in the Mildmay Tavern in the Balls Pond Road in Islington, where they played a date.  Howard and Blaikley were impressed by the group's lead vocalist, Dennis D'Ell, and the fact that they had a female drummer, Ann (‘Honey’) Lantree.  The group were looking for material to play for an audition with record producer Joe Meek, and they played the songs Howard and Blaikley had just given them.  Meek decided to record one of them, "Have I the Right?" , there and then.  Meek himself provided the B-side, "Please Don’t Pretend Again".

The Dark Side (DarkSun album): The Dark Side is the third studio album by power metal band DarkSun, which is the English version of "El Lado Oscuro", the album was released in September 2007.  "The Dark Side" and was released in September 2007 through FC Metal Recordings.  The critics were as good as the Spanish version, like "the album can be defined with one word: brilliant!" .  The band collaborated on Rage's album "Speak of the Dead", with a Spanish version of the song "Full Moon" entitled "La Luna Reine," which appeared as a bonus track.  Just after the release of "The Dark Side" drummer Rafael Yugueros left DarkSun to form part of power metal band WarCry replacing former drummer Alberto Ardines.  Yugueros had already worked with WarCry on their 1997's demo "Demon 97".  The band re-recruited Daniel Cabal who worked on what would become the band's new album "Libera Me".  On the summer of 2008 DarkSun announced that Cabalwas leaving the band, all these occurred in a professional and friendly way from both parties.  On the same announcement the band presented new drummer Jose Ojeda, who had performed drums on Spanish bands like Rivendel Lords, Killian, among others.

Dark Side of the Rainbow: Dark Side of the Rainbow – also known as Dark Side of Oz or The Wizard of Floyd – refers to the pairing of the 1973 Pink Floyd album "The Dark Side of the Moon" with the visual portion of the 1939 film "The Wizard of Oz."

Eva Orner: Eva Orner is an Australian, Academy and Emmy Award-winning film producer and director based in Los Angeles.  Her works include "Untold Desires" (winner of Best Documentary at the Australian Film Institute Awards, the Logie Awards and the Australian Human Rights Awards), "Strange Fits of Passion" (nominated for the Critics' Award at the Cannes Film Festival), "Taxi to the Dark Side" (winner of the 2008 Academy Award for Best Documentary), and "Gonzo, The Life and Work of Dr Hunter S. Thompson.  "Orner's directorial debut, "The Network", a feature documentary set behind the scenes of Afghanistan's largest television station, premiered in the US in March 2013.

A Life in the Death of Joe Meek: A Life in the Death of Joe Meek is an upcoming independent American documentary about the British record producer Joe Meek, made by Howard S. Berger and Susan Stahman.  Slated to be released October 2017.

Dark Side of the Moon Tour: The Dark Side of the Moon Tour was a concert tour by British rock band Pink Floyd in 1972 and 1973 in support of their album "The Dark Side of the Moon".  There were two separate legs promoting "Dark Side of the Moon", one in 1972 before the album's release and another in 1973 after its release.

Don Charles: Don Charles (10 December 1933 – 4 December 2005) was a popular English ballad singer, and record producer, and later in his life, a writer of a self-help book.  He is best known for his recordings of "Walk With Me My Angel" and "Bring Your Love to Me".  He also produced several of The Tornados' tracks including "Space Walk" and "Goodbye Joe".  The latter title referred his original mentor and producer, Joe Meek.  Meek regarded Charles highly.  "You are my only legit artist", Meek once informed Charles.  "All the others are yugga-dugs".  Standing at 6 ft , and weighing around seventeen stone (108 kilograms, 238 pounds), Charles stood out in more ways than one from his fellow performers.

Telstar: The Joe Meek Story: Telstar: The Joe Meek Story is a 2008 film adaptation of James Hicks' and Nick Moran's play "Telstar", about record producer Joe Meek, which opened at the New Ambassadors Theatre in London’s West End in June 2005.  The film is directed by Nick Moran and stars Con O'Neill, who also played Joe Meek in the original play, while Kevin Spacey plays Meek's business partner, Major Wilfred Banks.

Johnny Remember Me: "Johnny Remember Me" is a song which became a 1961 UK Single Chart #1 hit single for John Leyton, backed by The Outlaws.  It was producer Joe Meek's first #1 production.  Recounting the haunting – real or imagined – of a young man by his dead lover, the song is one of the most noted of the 'death ditties' that populated the pop charts, on both sides of the Atlantic, in the early to mid-1960s.  It is distinguished in particular by its eerie, echoing sound (a hallmark of Meek's production style) and by the ghostly, foreboding female wails that form its backing vocal, by Lissa Gray.  The recording was arranged by Charles Blackwell.  The song was banned by the BBC, along with many other 'death discs', which were popular at the time.

Taxi to the Dark Side: Taxi to the Dark Side is a 2007 American documentary film directed by Alex Gibney, and produced by him, Eva Orner, and Susannah Shipman.  It won the 2007 Academy Award for Best Documentary Feature.  It focuses on the December 2002 killing of an Afghan taxi driver named Dilawar, who was beaten to death by American soldiers while being held in extrajudicial detention and interrogated at the Parwan Detention Facility at Bagram air base.

Question: Which documentary has won more Academy Awards, Taxi to the Dark Side or A Life in the Death of Joe Meek?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "winning_documentary_title": {
      "type": "string",
      "description": "The title of the documentary that won more Academy Awards."
    },
    "documentary_comparison": {
      "type": "array",
      "description": "Details for each documentary compared.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the documentary."
          },
          "academy_awards_won": {
            "type": "integer",
            "description": "The number of Academy Awards won by the documentary."
          },
          "release_status": {
            "type": "string",
            "enum": [
              "released",
              "upcoming"
            ],
            "description": "The release status of the documentary."
          },
          "award_category": {
            "type": "string",
            "description": "The specific category of the Academy Award, if mentioned."
          }
        },
        "required": [
          "title",
          "academy_awards_won",
          "release_status"
        ],
        "additionalProperties": false
      }
    },
    "comparison_conclusion": {
      "type": "string",
      "description": "A brief conclusion stating which documentary won more awards."
    }
  },
  "required": [
    "winning_documentary_title",
    "documentary_comparison",
    "comparison_conclusion"
  ],
  "additionalProperties": false
}
