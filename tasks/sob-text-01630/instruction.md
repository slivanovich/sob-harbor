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
The Great War (documentary): The Great War is a 26-episode documentary series from 1964 on the First World War.  The documentary was a co-production of the Imperial War Museum, the British Broadcasting Corporation, the Canadian Broadcasting Corporation and the Australian Broadcasting Commission.  The narrator was Michael Redgrave, with readings by Marius Goring, Ralph Richardson, Cyril Luckham, Sebastian Shaw and Emlyn Williams.  Each episode is  40 minutes long.

5th Dimension – Secrets of the Supernatural: 5th Dimension – Secrets Of The Supernatural was a six episode documentary series that aired on Discovery Channel in 2006.  The episodes were 50 minutes in length.  The series was distributed by Parthenon entertainment, and was originally produced by German MPR Film und Fernsehproduktion GmbH in 2005.

The Day the Universe Changed: The Day the Universe Changed: A Personal View by James Burke is a British documentary television series written and presented by science historian James Burke, originally broadcast on BBC1 from 19 March until 21 May 1985 by the BBC.  The series' primary focus is on the effect of advances in science and technology on western society in its philosophical aspects.

Ken Kratz: Kenneth R. Kratz, also known as Ken Kratz, is a lawyer and the former district attorney of Calumet County, Wisconsin.  He gained prominence for trying a highly publicized homicide case, "State of Wisconsin v. Steven Avery" (2007), in which Avery and his nephew Brendan Dassey were both convicted.  This was the subject of "Making a Murderer" (2015), a Netflix 10-episode documentary series.

James Burke (science historian): James Burke (born 22 December 1936) is a British broadcaster, science historian, author, and television producer, who is known, among other things, for his documentary television series "Connections" (1978), and for its more philosophically oriented companion series, "The Day the Universe Changed" (1985), which is about the history of science and technology.  "The Washington Post" called him "one of the most intriguing minds in the Western world".

Lost Animals of the 20th Century: Lost Animals of the 20th Century is a 16-episode documentary series shown on the Discovery Channel in the 1990s.  It features animals that have become extinct throughout the 20th century.  Animals are adjudged as such when the last specimen of the species dies sometime from 1901 to 2000.  However, since the show was produced in the 1990s (still part of the 20th century), most of the animals covered became extinct in the early part of the century.  Greta Scacchi introduces each episode during the title sequence and narrates episodes 1 through 8.  Lin Sagovsky narrates the remainder of the series.

The Naked Pilgrim: The Naked Pilgrim is documentary series produced by British broadcaster Five and presented by art critic Brian Sewell.  First broadcast in 2003, the series follows Sewell on the Catholic pilgrimage to Santiago de Compostela.

Richard Hammond's Engineering Connections: Richard Hammond's Engineering Connections is a documentary series originally broadcast on the National Geographic Channel, and later on BBC2.  It is presented by Richard Hammond, and looks at how engineers and designers use historic inventions and clues from the natural world in ingenious ways to develop new buildings and machines.  The show's format is very similar to that of James Burke's 1978 documentary series, "Connections".  The first series premièred on 8 September 2008, on National Geographic, and on 1 March 2010, on BBC2.  The first series contained four episodes.  The second series premièred on 7 September 2009, on National Geographic, and on 8 May 2010, on BBC2.  The second series contained six episodes.  The third series premièred on 8 May 2011, on BBC2 and contained six episodes.  The BBC2 broadcasts of the first two series have a slightly shorter running time and contain less information than the original National Geographic broadcasts, with on average one minute of footage cut from every episode.  None of the three series of the programme are available to purchase on DVD in the UK, however, all three can be watched on demand for subscribers of National Geographic on Sky, Virgin Media and BT Vision.  In Australia, all three series are available on DVD, either separately or as a box-set.

Journey Through the Solar System: Journey Through the Solar System was a 13-episode documentary series produced by NASA's Lewis Research Center in 1983.  Each half-hour episode contained the entirety or clips of older NASA films with framing host footage with Larry Ross, Director of Space Science at Lewis.

Connections (TV series): Connections is a 10-episode documentary television series and 1978 book ("Connections", based on the series) created, written, and presented by science historian James Burke.  The series was produced and directed by Mick Jackson of the BBC Science and Features Department and first aired in 1978 (UK) and 1979 (USA).  It took an interdisciplinary approach to the history of science and invention, and demonstrated how various discoveries, scientific achievements, and historical world events were built from one another successively in an interconnected way to bring about particular aspects of modern technology.  The series was noted for Burke's crisp and enthusiastic presentation (and dry humour), historical re-enactments, and intricate working models.

Question: What year did the 10-episode documentary series by British broadcaster James Burke premiere in the U.K.?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_series_title": {
      "type": "string",
      "description": "The title of the documentary series."
    },
    "episode_count": {
      "type": "integer",
      "description": "The total number of episodes in the series."
    },
    "presenter_name": {
      "type": "string",
      "description": "The name of the series presenter."
    },
    "presenter_nationality": {
      "type": "string",
      "description": "The nationality of the presenter."
    },
    "premiere_year_uk": {
      "type": "integer",
      "description": "The year the series first aired in the U.K."
    }
  },
  "required": [
    "documentary_series_title",
    "episode_count",
    "presenter_name",
    "presenter_nationality",
    "premiere_year_uk"
  ],
  "additionalProperties": false
}
