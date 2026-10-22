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
Dan Cortese: Daniel James "Dan" Cortese (born September 14, 1967) is an American actor.  He played Perry Rollins on "Veronica's Closet" and Vic Meladeo on "What I Like About You".

My Dad Is Better Than Your Dad: My Dad Is Better Than Your Dad was a reality sports TV show on NBC that premiered on February 18, 2008.  The show was produced by Mark Burnett, producer of other shows like "Survivor", "The Apprentice", and "Are You Smarter Than a 5th Grader? ", and was hosted by actor Dan Cortese.  Four teams of children and their fathers competed in each episode, with the winning team having the chance to win up to $50,000.

John Amos: John Allen Amos Jr. (born December 27, 1939) is an American actor who is best known for his role as James Evans, Sr. on the CBS television series "Good Times" (1974–76).  Amos' other television work includes roles in "The Mary Tyler Moore Show", the miniseries "Roots", for which he received an Emmy nomination, and a recurring role as Admiral Percy Fitzwallace on "The West Wing".  Amos also played the father of Will Smith's character's girlfriend, Lisa Wilkes, in "The Fresh Prince of Bel-Air", and he had a recurring role on "In the House" with LL Cool J, as Coach Sam Wilson.  Amos played the Father of Tommy Strawn (Thomas Mikal Ford) on the long running sitcom, "Martin", as Sgt. Strawn, and another recurring role on "Two and a Half Men" as Chelsea's dad's new lover, Edward Boynton.  Amos also played Major Grant, the US Special forces officer in "Die Hard 2".  Amos has also appeared on Broadway and in numerous films in a career that spans four decades.  He has received nominations for a Primetime Emmy Award and NAACP Image Award.

Peanut Louie Harper: Mareen Louie Harper ("née" Louie; born August 15, 1960), better known by her nickname Peanut, is a retired American female tennis player, born in San Francisco, California to Ron and Alice Louie.  Her elder sister, Marcie, also played on the WTA Tour, while her sisters Cici and Marisa, and brother Ronnie, all played at the University of San Francisco.  She, along with her siblings, trained on the tennis courts of Golden Gate Park.  She was given the nickname "Peanut" by her dad because she was the youngest of the five children.

Dad's Army: Dad's Army is a BBC television sitcom about the British Home Guard during the Second World War.  It was written by Jimmy Perry and David Croft, and broadcast on the BBC from 1968 to 1977.  The sitcom ran for nine series and 80 episodes in total; there was also a radio version based on the television scripts, a feature film and a stage show.  The series regularly gained audiences of 18 million viewers, and is still repeated worldwide.

Gage Clarke: Gage Clarke (March 3, 1900 – October 22, 1964) was an American character actor best known for his role as the principal in "Mister Peepers".  His other work consisted largely of one-shot appearances in television series such as seven major supporting roles as different characters in "Maverick", twelve roles in "Gunsmoke" (Clarke played a key role in the "Maverick" spoof of "Gunsmoke", an episode entitled "Gun-Shy"), "Mister Ed", "Laramie", "Ben Casey", "Checkmate", "The Twilight Zone", "The Real McCoys" (twice), four roles in "Alfred Hitchcock Presents", "Bourbon Street Beat", "Thriller", "Have Gun Will Travel", and many others, as well as movies including "I Want to Live! ", "The Bad Seed", "The Brothers Karamazov", and "The Absent-Minded Professor".  Clarke, a slightly overweight actor with a double chin, specialized in playing avuncular, rather timid characters, with one of his largest parts being frightened gambler "Foursquare Farley" in the "Maverick" episode "Greenbacks, Unlimited" opposite James Garner and John Dehner.  He made two guest appearances on "Perry Mason", including the role of Frederick Rollins in "The Case of the Glittering Goldfish" in 1959.  He also played the part of Mr. Murg in "Pollyanna" in 1960.

Zerick Rollins: Zerick Rollins was born June 20, 1975 in Houston, Texas.  Zerick Rollins has been as assistant coach for the Seattle Seahawks for the last nine years.  Rollins coached linebackers for the last three years (2006–2009).  Prior to coaching linebackers for Seattle Rollins coached the defensive line for four years (2002–2006).  Rollins started his career in Seattle as a defensive line assistant in 2001.  Prior to coming to the Seattle Seahawks, Rollins was a graduate assistant (1998–2000) and played college football for Texas A&M.  Zerick was a two-year starter at Texas A&M (1996–1997) where he helped Texas A&M win the Big 12 South title in 1997.  He also played in the 1998 Cotton Bowl against UCLA.

Mervyn Grell: Mervyn George Grell , Major E.D. Had served with the British West Indies Regiment in France during WW1.  He also served with the Local Trinidad Regiment (T'dad, Volunteers) in WW II.  Between these dates he played Cricket. - A hard-hitting, lower-order batsman and a medium pace bowler, Mervyn Grell was born in Trinidad on 18 December 1899 and died in Cocorite on the same Caribbean island on 11 January 1976, aged 77.  In a career spanning the years 1930 to 1937, he played only a handful of first-class matches, ten in total.  Half of these were against the visiting M.C.C. including his debut, played at Port-of-Spain in January 1930 in which he performed admirably when scoring 40 and 54 batting at number 9 and 8 respectively; he top-scored in Trindad's first innings and was their second highest scorer in the second.  He also took the wickets of N.E. Haig and L.F. Townsend in the visitor’s second innings, both players caught by wicketkeeper Errol Hunte.  In just his second match, also played against the M.C.C. in Port-of-Spain, Grell was asked to captain Trinidad and followed a duck in the first innings with his team’s top-score in the second, 34 not out.  This particular score led a rearguard action that almost brought victory.  On the basis of the three scores that he had achieved against F.S.G. Calthorpe’s team, and because of his proximity to the ground (the West Indies liked to keep travel costs down to a minimum!) , he was selected to play in the second Test against England, played at Port-of-Spain in February, 1930.  By scoring 21 and 13 he far from disgraced himself in West Indies’ defeat but he was never picked to play for his country again.  In all first-class matches, Grell recorded his highest score, 74 not out, in his last, played at Bourda, Georgetown against British Guiana in 1937.  Contrary to normal practice, no obituary appeared within the pages of Wisden after Grell's death.

Julia Hills: Julia Hills (born 3 April 1957) is an English actress best known for playing the man hungry Rona in eight series of the BBC hit sitcom "2point4 Children".  She also played all of the women and some of the men in Channel 4's first late night satirical sketch show "Who Dares Wins", Beryl in two series of the sitcom "Dad" with Kevin McNally and Caroline Joyner in "Casualty".

Quinten Rollins: Quinten Benjamin Frederick Rollins (born July 15, 1992) is an American football cornerback for the Green Bay Packers of the National Football League (NFL).  He played college football at Miami University (Ohio), where he also played college basketball.  Rollins was drafted in the second round of the 2015 NFL Draft

Question: In what sitcom does the host of My Dad Is Better Than Your Dad also played Perry Rollins? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "host_name": {
      "type": "string",
      "description": "The name of the host of 'My Dad Is Better Than Your Dad'."
    },
    "show_hosted": {
      "type": "string",
      "description": "The name of the show hosted by the person."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the host."
    },
    "sitcom_name": {
      "type": "string",
      "description": "The name of the sitcom where the character was played."
    }
  },
  "required": [
    "host_name",
    "show_hosted",
    "character_played",
    "sitcom_name"
  ],
  "additionalProperties": false
}
