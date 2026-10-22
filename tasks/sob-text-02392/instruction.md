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
Bernal Heights Summit: Bernal Heights Summit ( ) or Bernal Heights Hill is a hill in the San Francisco, California neighborhood of Bernal Heights.  Upper elevations are part of Bernal Hill Park, a component of San Francisco Recreation and Parks.  At the highest elevation is a privately owned site, which contains an equipment building and 50-foot tall telecommunications tower, which is currently unnamed.  The park and summit are largely surrounded by Bernal Heights Boulevard.

Carpenter Hill: Carpenter Hill is a hill located in the eastern Sacramento Valley-Sierra Nevada foothills region of California.  The hill, located within the city limits of Folsom, near the Sacramento-El Dorado county line and north of U.S. Route 50, rises to an elevation of 828 ft .  Despite its low elevation, the hill is the county highpoint of Sacramento County and thus the summit offers expansive views of the Central Valley.

Baldy Mesa: Baldy Mesa is a summit whose tallest peaks on its southern extremity, overlook the upper Cajon Canyon in San Bernardino County, California.  Its tallest point is an unnamed 4,964 foot high hill on the southwest end of the mesa overlooking the upper Cajon Canyon.  The heights that lie along the ridge overlooking the canyon toward the east gradually descend in elevation from one approximately 4,770 feet to the 4,606 foot hill at its far southeastern end at .  The mesa descends gradually in elevation to the north, toward the distant Mohave River.  it is bounded on the east by the Oro Grande Wash.

Cavanal Hill: Cavanal Hill (officially Cavanal Mountain), located near Poteau, Oklahoma, is billed by a local chamber of commerce as the, "tallest hill in the world", because the elevation of its summit is 1999 ft .  The actual summit elevation is 2385 ft above sea level; the difference in elevation between the summit and the Poteau River 3 mi to the north is 1960 ft .

Bear Mountain (Connecticut): Bear Mountain, is a prominent peak of the southern Taconic Mountains.  It lies within the town of Salisbury, Connecticut, in the United States, and is the highest mountain "summit" in the state of Connecticut.  The highest "point" in the state, however, is located on the south slope of Mount Frissell 1.3 mi to the west at 2379 ft .  Much of the mountain is protected as part of the viewshed and corridor of the Appalachian National Scenic Trail, which crosses the summit grounds.  From the summit the view includes Twin Lakes and cultivated fields to the east, the Catskills and nearby Taconic peaks to the west, and Massachusetts' Mount Everett and Mount Race to the north.  Though the mountain's elevation is commonly reported at 2316', the elevation near its stone monument tower, the proper summit lies approximately 125 feet northwest of the tower, accessible by a herd path following the mountain's abandoned Bee Line Trail to the Northwest Camp owned by the Connecticut Chapter of the Appalachian Mountain Club.  The mountain is noted for its old growth scrub forest of pitch pines, birch, oak and other short-statured trees, much like its neighbors, Mounts Everett and Race, for its numerous wild blueberry bushes which produce in late July and early August, and for its rattlesnakes, which in summer are sometimes seen sunning themselves on the mountain's numerous open rocks of mica, schist and gneiss.

Two Point Mountain (Idaho): Two Point Mountain is the highest point in the Boise Mountains with a summit elevation of 10124 ft located in the Fairfield Ranger District of Sawtooth National Forest, Idaho.  It is located 12.67 mi from Perfect Peak in the Sawtooth Range, its line parent, giving it a prominence of 1524 ft .  Two Point Mountain is named for having two peaks: its main summit and a second summit about 0.4 mi to the northwest that rises to an elevation of 10060 ft .  The mountain is within the watershed of the South Fork Boise River where the south side is drained by Bear Creek and the north side by the Rosss Fork.  No maintained trails lead to either summit.

Lanfair Buttes: Lanfair Buttes, also known as Eagle Mountain, Indian Hill, Eagle Hill, Graveyard Hills is a summit in the Mojave National Preserve in the Mojave Desert in San Bernardino County, California.  The Lanfair Buttes lie 3 miles (4.8 km) east-southeast of the Grotto Hills and 8 miles (13 km) north-northeast of Hackberry Mountain in Lanfair Valley.  The tallest and northernmost elevation in the Lanfair Buttes is Eagle Mountain at 1338 feet.  The southernmost elevation is Indian Hill, at at an elevation of 1281 feet.  Indian Well, an old well is found west of the Buttes at , and petroglyphs are found nearby on the slope of the Buttes to the east.  Indian Well petroglyphs indicate it was a Native American water source and camping site in previous centuries.  Indian Well was also located along the route of the Mohave Trail.

Roughlee: Roughlee is a village in Pendle, Lancashire, England, in the civil parish of Roughlee Booth.  It is close to Nelson, Barrowford and Blacko.  The village lies at the foot of Pendle Hill, well known for the Pendle Witches, and includes the hamlet of Crowtrees.  The parish adjoins the Pendle parishes of Blacko, Barrowford, Old Laund Booth, Goldshaw Booth and Barley-with-Wheatley Booth.  It is part of the Forest of Bowland Area of Outstanding Natural Beauty (AONB).

Pendle Hill: Pendle Hill is located in the east of Lancashire, England, near the towns of Burnley, Nelson, Colne, Clitheroe and Padiham.  Its summit is 557 m above mean sea level.  It gives its name to the Borough of Pendle.  It is an isolated hill, separated from the Pennines to the east, the Bowland Fells to the northwest, and the West Pennine Moors to the south.  It is included in detached part of the Forest of Bowland Area of Outstanding Natural Beauty (AONB).

Ancon Hill: Ancon Hill is a 654-foot hill that overlooks Panama City, Panama, adjacent to the township of Ancón.  Ancón Hill is an area in Panama that was used for administration of the Panama Canal.  It was under U.S. jurisdiction as part of the Panama Canal Zone until being returned to Panama in 1977.  Largely undeveloped, the area is now a reserve.  The hill includes the highest point in Panama City.  The summit of the hill can be reached by a 30-minute hike.  According to a local Ancon resident, at this time it is no longer possible to drive to the summit of Cerro Ancon (February 12, 2017).  Relatively undeveloped it includes jungle in an otherwise urban area, and wildlife still survives cut off from other jungle areas.  It is not uncommon to see sloths, white-nosed coati, nine-banded armadillos, Geoffroy's tamarins, or deer on Ancon Hill, which now has protected status.  Its name is used as an acronym by a Panamanian environmental group, Asociación Nacional para la Conservación de la Naturaleza (ANCON).

Question: Roughlee is located located at the foot of the hill that has a summit of what elevation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_name": {
      "type": "string",
      "description": "The name of the village."
    },
    "hill_name": {
      "type": "string",
      "description": "The name of the hill associated with the village."
    },
    "summit_elevation": {
      "type": "object",
      "properties": {
        "value": {
          "type": "integer",
          "description": "The numerical value of the summit elevation."
        },
        "unit": {
          "type": "string",
          "description": "The unit of measurement for the summit elevation (e.g., 'm', 'ft')."
        }
      },
      "required": [
        "value",
        "unit"
      ],
      "additionalProperties": false
    },
    "location_relationship": {
      "type": "string",
      "description": "Describes the geographical relationship between the village and the hill."
    }
  },
  "required": [
    "village_name",
    "hill_name",
    "summit_elevation",
    "location_relationship"
  ],
  "additionalProperties": false
}
