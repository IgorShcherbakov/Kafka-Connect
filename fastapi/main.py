import uvicorn
from fastapi import FastAPI, Response
from jinja2 import Template


app = FastAPI()


@app.get("/")
def root_route():
   return "FastAPI"


@app.get("/item/{item_id}")
def item_route(item_id: str):
   return f"item = {item_id}"

@app.get("/metrics")
def get_metrics():
   json_example = {
      "Alloc": {
         "Type": "gauge",
         "Name": "Alloc",
         "Description": "Alloc is bytes of allocated heap objects.",
         "Value": 24293912
      },
      "FreeMemory": {
         "Type": "gauge",
         "Name": "FreeMemory",
         "Description": "RAM available for programs to allocate",
         "Value": 7740977152
      },
      "PollCount": {
         "Type": "counter",
         "Name": "PollCount",
         "Description": "PollCount is quantity of metrics collection iteration.",
         "Value": 3
      },
      "TotalMemory": {
         "Type": "gauge",
         "Name": "TotalMemory",
         "Description": "Total amount of RAM on this system",
         "Value": 16054480896
      }
   }
   metrics = list(json_example.values())
   metrics_template = """
   {% for metric in metrics %}
   # HELP {{metric.Name}} {{metric.Description}}
   # TYPE {{metric.Name}} {{metric.Type}}
   {{metric.Name}} {{metric.Value}}
   {% endfor %}
   """
   try:
      template = Template(metrics_template)
      result = template.render(metrics=metrics).strip()
   except Exception as e:
      result = str(e)

   # Удаляем лишние пробелы и табуляции
   result = "\n".join(line.strip() for line in result.splitlines() if line.strip())
   
   return Response(media_type="text/plain", content=result)


if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8085) 