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
New River Gorge National River: The New River Gorge National River is a unit of the United States National Park Service designed to protect and maintain the New River Gorge in southern West Virginia.  Established in 1978, the NPS-protected area stretches for 53 mi from just downstream of Hinton to Hawks Nest State Park near Ansted.

Loomis Museum: The Loomis Museum, also known as the Loomis Visitor Center, the Manzanita Lake Visitor Center and the Manzanita Lake Museum, was built by Benjamin Franklin Loomis in 1927 near Manzanita Lake, just outside Lassen Volcanic National Park in California, USA.  Loomis was a local homesteader and photographer who documented the 1915 eruptions of Lassen Peak, and was instrumental in the 1916 establishment of the national park.  In 1929 Loomis donated the museum and 40 acre of surrounding lands to the National Park Service, which since then has used the structure as an interpretational facility.

Logan Pass Visitor Center: The Logan Pass Visitor Center in Glacier National Park was constructed at the summit (Logan Pass) of the Going-to-the-Sun Road during the Mission 66 park facilities improvement program.  The design concept was originated by architect Cecil J. Doty of the National Park Service Western Office of Design and Construction.  Burt L. Gewalt of the Kalispell, Montana architectural firm Brinkman and Lenon was responsible for the construction documents, carried out between 1960 and 1962.  Construction was completed in 1966.  The visitor center uses common Mission 66 themes such as a broad, gently sloping roof, native stone, and glulam timber construction.

Bank of Glen Jean: The Bank of Glen Jean is located in the unincorporated community of Glen Jean, West Virginia.  The bank was the financial center of a railroading, mining and financial conglomerate belonging to William McKell, son of Thomas G. and Jean McKell, the town's namesake.  Built in 1909, the bank operated until 1939.  It is now a visitor contact center for New River Gorge National River.

Gettysburg National Museum: The Gettysburg National Museum was a Gettysburg Battlefield visitor attraction on the south border of the Gettysburg borough.  Established by George D. Rosensteel after working at his uncle's 1888 Round Top Museum, the facility had an interpretive Battle of Gettysburg map using incandescent lights and was acquired by the National Park Service for use as the 1974–2008 Gettysburg National Military Park museum and visitor center after the Cyclorama Building at Gettysburg and before the Gettysburg Museum and Visitor Center.

Quarry Visitor Center: Quarry Visitor Center, in Dinosaur National Monument in Utah was built as part of the National Park Service's Mission 66 program of modern architectural design in the US national parks.  This visitor center exemplifies the philosophy of locating visitor facilities immediately at the resource being interpreted.  The visitor center was closed from 2006 to 2011 due to structural damage from unstable soils.  The rotunda structure was demolished and replaced with a new structure of different design, while the quarry section was being stabilized and repaired.

Alpine Visitor Center: Rocky Mountain National Park's Alpine Visitor Center is located at 11,796 feet (3,595 m) above sea level at Fall River Pass, one mile west of the highest point on Trail Ridge Road and four miles east of the Continental Divide at Milner Pass in the U.S. state of Colorado.  It is the highest visitor center in the National Park System.

Golden West Visitor Center: The Golden West Visitor Center is located at the southeast unit of North Cascades National Park Complex in the Lake Chelan National Recreation Area.  It sits at the southern end of the small town of Stehekin, Washington and is the only National Park Service visitor center in the southeast unit of the Park Complex.  It is the main ranger station for all traffic in and out from the south end of the park via boat, seaplane or by foot from the many hiking trails linking the Stehekin River Valley to the outside world.

Sites Homestead: The Sites Homestead, also known as the Wayside Inn or the Sites Inn, is located near Seneca Rocks, West Virginia.  The log house was built by Jacob Sites "circa" 1839 below the Seneca Rocks ridge.  The house was expanded in the mid-1870s with a frame addition, remaining in the Sites family until it was acquired by the U.S. Forest Service in 1968 as part of Spruce Knob-Seneca Rocks National Recreation Area in Monongahela National Forest.  The house had been used as a storage shed for some time and was in poor condition.  It was restored by the Forest Service in the 1980s and became a temporary visitor center in 1992 after the Seneca Rocks visitor center burned.  It is now part of the Seneca Rocks Discovery Center facility, operated by the Forest Service.

Wallops Flight Facility Visitor Center: The Wallops Flight Facility Visitor Center is located in Building J-17, Wallops Island, Virginia, United States along Route 175.  It contains exhibits highlighting past missions conducted at NASA's Wallops Flight Facility.  The visitor center also provides information about current activities at Wallops Flight Facility, such as the sounding rocket, balloon and aircraft program.  The outside grounds has a rocket garden consisting of rockets and aircraft used for space and aeronautical research, including a full-scale four stage reentry vehicle used to study the Earth's atmosphere.  In addition, the visitor center has educational programs on Earth and space science.  It is also a viewing area for rocket launches.

Question: The building once occupied by the bank in Glen Jean, West Virginia now houses a visitor center for which feature of the National Park there?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "building_name": {
      "type": "string",
      "description": "The name of the building that now houses the visitor center."
    },
    "original_purpose": {
      "type": "string",
      "description": "The original purpose or function of the building."
    },
    "current_purpose_description": {
      "type": "string",
      "description": "A description of the building's current use."
    },
    "location": {
      "type": "object",
      "properties": {
        "community": {
          "type": "string",
          "description": "The community where the building is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the building is located."
        }
      },
      "required": [
        "community",
        "state"
      ],
      "additionalProperties": false
    },
    "national_park_service_unit_served": {
      "type": "string",
      "description": "The name of the National Park Service unit that the visitor center serves."
    }
  },
  "required": [
    "building_name",
    "original_purpose",
    "current_purpose_description",
    "location",
    "national_park_service_unit_served"
  ],
  "additionalProperties": false
}
