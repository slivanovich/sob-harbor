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
Martin Gantner: Martin Gantner is a German operatic baritone.  He made his professional opera debut in Koblenz as Count Almaviva in "The Marriage of Figaro".  He soon after joined the roster of singers at the Deutsche Oper Berlin where he notably portrayed one of the gang members in the world premiere of Hans Werner Henze's "Das verratene Meer" in 1990; a part he reprised for his debut at La Scala.  Engagements with other important houses soon followed, including the Semperoper (Dandini in "La Cenerentola") and Theater Basel (Guglielmo in "Così fan tutte").  He has been a member of the Bavarian State Opera since 1993.  Other companies with whom he has appeared as a guest artist include the Berlin State Opera, the Cologne Opera, the Deutsche Oper am Rhein, La Monnaie, the Liceu, the Los Angeles Opera, the Lyric Opera of Chicago, the Vienna State Opera, and the Zurich Opera among others.

Diamonds and Pearls: Diamonds and Pearls is the thirteenth studio album by American recording artist Prince, and the first with his backing band The New Power Generation.  It was released on October 1, 1991 by Paisley Park Records and Warner Bros.  Records.  The album produced several hit singles, including "Gett Off", "Cream", "Money Don't Matter 2 Night", "Insatiable", and the title track.  Dancers Lori Werner (then dancing under the stage name of Lori Elle) and Robia LaMorte, known as "Diamond" and "Pearl" respectively, appeared on the holographic cover (re-pressings of the album are non-holographic).  Diamond and Pearl also appeared in the music videos for "Cream", "Strollin'", "Gett Off", and the title track, and also participated in Prince's Diamonds and Pearls Tour.

Werner Pledath: Werner Pledath (26 April 1898 – 6 December 1965) was a German actor who appeared in many films during a lengthy career.  He generally played supporting roles such as in "Five from the Jazz Band" (1932).  Pledath specialized in playing powerful, authority figures.  Following the Second World War he appeared in several films made in East Germany.

Smokescreen (Marvel Comics): Smokescreen is a fictional character that appeared in comic books published by Marvel Comics.  A criminal looking to take over the illegal gambling business.  He appears in the public service comic "Spider-Man Storm and Power Man Battle Smokescreen" to aware readers of the dangers of smoking.  He momentarily captures Storm then is captured by Spider-Man with the assistance of Power Man who then hand him over into police custody.

Maria Bard: Maria Bard (7 July 1900 – 8 April 1944) was a German stage actress, who made a handful of films in the silent era for Rimax, her first husband Wilhelm Graaff's company.  By 1930, her marriage with Graaff was over, and she appeared with Werner Krauss in the stage production "Der Kaiser von Amerika" or "The King of America" and the two became involved.  Unfortunately, Krauss' wife discovered their affair and committed suicide; a year later, in 1931, Maria Bard married Werner Krauss.  Her third husband was actor Hannes Stelzer.  Bard committed suicide on 8 April 1944, apparently for political reasons.  On December 27, 1944, toward the end of World War II, Stelzer who was in the Luftwaffe at this point, died when his plane was shot down over the Eastern front.

Werner Daehn: Werner Daehn (born 14 October 1967) is a German actor with an international reputation, who has worked with Vin Diesel and Samuel L. Jackson in "XXX", with Jason Priestley in "Colditz" an ITV1 2005 miniseries, with Bill Pullman in "Revelations" and with Steven Seagal in "Shadow Man".  In addition he has also worked in German productions like "Stauffenberg - Rebellion of Conscience" (also titled "Valkeryie" on the German DVD) and "" (nominated in Germany for the ).  He appears momentarily in the film "The Lives of Others" by Florian Henckel von Donnersmarck.  He also took part in a British production for the BBC, when in 2011 he played the role of Dr Georg Maurer, the German doctor who treated the Manchester United players who survived the 1958 Munich air disaster.  In 2016, he played the role of Josef Von Zimmerman, in Game of Aces.

The Lives of Others: The Lives of Others (German: "Das Leben der Anderen" ) is a 2006 German drama film, marking the feature film debut of filmmaker Florian Henckel von Donnersmarck, about the monitoring of East Berlin residents by agents of the Stasi, the GDR's secret police.  It stars Ulrich Mühe as Stasi Captain Gerd Wiesler, Ulrich Tukur as his superior Anton Grubitz, Sebastian Koch as the playwright Georg Dreyman, and Martina Gedeck as Dreyman's lover, a prominent actress named Christa-Maria Sieland.

Mimi Werner: Mimmi Michaela Sarah Werner (born 17 December 1990), better known as Mimi Werner, is a Swedish singer and songwriter.  In 2015, she got signed to Sony Music Sweden, and travelled to Nashville to work on her first album.  Her debut single called "Forever Again" was released in 2015.  Werner participated in Melodifestivalen 2016 with the song "Ain't No Good", she was however eliminated in the first semi-final placing fifth.

Game of Aces: Game of Aces is a 2016 World War I action film written and directed by Damien Lay, in his debut in helming a fiction feature.  The film stars Chris Klein, Victoria Summer and Werner Daehn whose role is as a German double-agent with all of his dialogue in German with English subtitles; Summer also speaks German for most of the film.

King of Thieves (film): King of Thieves is a 2004 movie directed by Ivan Fíla, starring Lazar Ristovski, Jakov Kultiasov, Katharina Thalbach, Paulus Manker, Birol Ünel and Werner Daehn.

Question: In who's debut Werner Daehn appeared momentarily?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor whose appearance is being described."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film in which the actor appeared."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director whose debut the film marked."
    },
    "director_debut_type": {
      "type": "string",
      "description": "The type of debut the film represented for the director (e.g., feature film debut)."
    },
    "appearance_detail": {
      "type": "string",
      "description": "A description of the actor's appearance in the film, e.g., 'momentarily'."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "director_name",
    "director_debut_type",
    "appearance_detail"
  ],
  "additionalProperties": false
}
