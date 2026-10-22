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
Bradley Cooper: Bradley Charles Cooper (born January 5, 1975) is an American actor.  He was one of the world's highest-paid actors for three years, and has been nominated for various accolades, including four Academy Awards, two BAFTA Awards and two Golden Globe Awards.  Cooper appeared in "Forbes" Celebrity 100 on two occasions and "Time"'s list of 100 most influential people in the world in 2015.

Golu Hadawatha: Golu Hadawatha (Translation: Silence of the Heart) was a popular 1968 Sinhalese language romance movie directed by Maestro Lester James Peiris.  Wickrema Bogoda and Anula Karunathilake act the lead roles of Sugath (Sugath Weerasekera) and Dhammhi (Dhamayanthi Kariyawasam).  The movie's story is built on the novel Golu Hadawatha written by Karunasena Jayalath in 1962, based on his school time experiences and memories.  Regi Siriwardena wrote the screenplay and Veteran Sinhala musician Premasiri Khemadasa composed the music.  Golu Hadawatha is acclaimed as a movie that set a milestone in Sinhala moviemaking.  It introduced a new cinematic format to the romance and love movie genre.  The movie departs from the then traditional movie style; no hero, heroine,("Boy" and "Girl") no enemy or villain, Joker, no songs, and fights etc.  Based on a romantic and emotional attachment between a teenage boy and a girl who study in the same class of their school, Golu Hadawatha is regarded as one of the landmarks in Sri Lankan Cinema.

AFI's 100 Years...100 Movie Quotes: Part of The American Film Institute (AFI 100 Years... series), AFI's 100 Years... 100 Movie Quotes is a list of the top 100 movie quotations in American cinema.  The American Film Institute revealed the list on June 21, 2005, in a three-hour television program on CBS.  The program was hosted by actor Pierce Brosnan and had commentary from many Hollywood actors and filmmakers.  A jury consisting of 1,500 film artists, critics, and historians selected "Frankly, my dear, I don't give a damn," spoken by Clark Gable as Rhett Butler in the 1939 American Civil War epic "Gone with the Wind" as the most memorable American movie quotation of all time.

Mattupetti Machan: Mattupetty Machan is a 1998 Malayalam movie directed by Jose Thomas.  Mukesh, Baiju, Kalabhavan Navas, Jagathy Sreekumar, Oduvil Unnikrishnan, Maathu etc. played the main roles in the movie.  The movie was produced by Gopikrishnan, Vinu Kiriyath and Kannan Nair under the banner of Gopurachithra who also distributed the movie.  Rajan Kiriyath and Vinu Kiriyath created the story for which the script and direction was added by Udaykrishna and Siby K. Thomas.  The film is considered as an All time Block Buster in Mukesh's career and was remade in Tamil as "Banda Paramasivam" with Prabhu and Rambha, remade in Telugu as "Hungama" with Ali and Venu Madhav.  Bollywood blockbuster "Housefull 2" was an uncredited remake of "Mattupetti Machan".

Guardians of the Galaxy (film): Guardians of the Galaxy (retroactively referred to as Guardians of the Galaxy Vol.  1) is a 2014 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the tenth film in the Marvel Cinematic Universe.  The film was directed by James Gunn, who wrote the screenplay with Nicole Perlman, and features an ensemble cast including Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel, Bradley Cooper, Lee Pace, Michael Rooker, Karen Gillan, Djimon Hounsou, John C. Reilly, Glenn Close, and Benicio del Toro.  In "Guardians of the Galaxy", Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact.

The 100th Love with You: The 100th Love with You, known in Japan as Kimi to Hyakkaime no Koi (君と100回目の恋 , The 100th Love with You ) , is a movie directed by Sho Tsukikawa starring the Japanese artist and singer miwa and actor Kentarō Sakaguchi.

Hit List (1989 film): Hit List is a 1989 action–thriller movie directed by William Lustig.  The tagline for the movie was: ""They attacked the wrong woman... They kidnapped the wrong child... And they made the wrong man their target.""  The film was produced by Cinetel Films and was distributed in US theaters by New Line Cinema and in Canadian theaters by Cineplex Odeon Films and on VHS format by RCA/Columbia Pictures Home Video, but has been out of print for some time.  As of December 26, 2009, Sony has not announced any plans to release a DVD of the movie.  The movie was referenced in the movie "Urban Legend" (1998).

Time 100: Time" 100 (often written in all-caps as TIME" 100) is an annual list of the 100 most influential people in the world assembled by the American news magazine "Time".  First published in 1999 as the result of a debate among American academics, politicians, and journalists, the list is now an annual event.  Although appearing on the list is often seen as an honor, "Time" makes it clear that entrants are recognized for changing the world, regardless of the consequences of their actions.  The final list of influential individuals is exclusively chosen by "Time" editors with nominations coming from the "TIME" 100 alumni and the magazine's international writing staff.  Only the winner of the Reader's Poll, conducted days before the official list is revealed, is chosen by the general public.

Sapne Sajan Ke: Sapne Saajan Ke is 1992 Hindi language movie directed by Lawrence D'Souza and starring Karishma Kapoor, Rahul Roy, and Jackie Shroff.  The movie was a collaboration of director Lawrence D'Souza and producer Sudhakar Bokade after their blockbuster movie Saajan.  However, the movie was average earner at box office.  Actor Aditya Pancholi used his voice to promote the movie as another movie after super success of movie Saajan

Phaansi: Phaansi is a 1978 Hindi movie directed by Harmesh Malhotra.  The film stars Shashi Kapoor, Sulakshana Pandit, Pran and Ranjeet.  The film's music is by Laxmikant Pyarelal.  Actor Asrani has also played a role as a Muslim guy in the movie who was a closed friend to Shashi Kapoor and actor Iftikar played role as father to Shahsi Kapoor.  Unfortunately, both of them was hanged to death by the villain (Ranjeet).  Thumbs up for Ranjeet of acting the role of Chief of Daku in the movie.The movie was declared hits due to its story line, drama, songs and good action.  A worth to watch movie of the 1970s.

Question: An actor on Time's list of 100 most influencial poeple stared in a movie directed by who? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who was on Time's list of 100 most influential people."
    },
    "time_list_year": {
      "type": "integer",
      "description": "The year the actor appeared on Time's list."
    },
    "movie_details": {
      "type": "object",
      "properties": {
        "movie_title": {
          "type": "string",
          "description": "The title of the movie the actor starred in."
        },
        "director_name": {
          "type": "string",
          "description": "The name of the director of the movie."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the movie."
        }
      },
      "required": [
        "movie_title",
        "director_name",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "time_list_year",
    "movie_details"
  ],
  "additionalProperties": false
}
