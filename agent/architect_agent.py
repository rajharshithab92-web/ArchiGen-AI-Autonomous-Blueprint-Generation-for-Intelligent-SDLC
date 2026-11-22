import json
import os
import re
import html


class ArchiGenAgent:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.dataset_path = os.path.join(project_root, "knowledge", "ecommerce.json")
        with open(self.dataset_path, "r", encoding="utf-8") as file:
            self.knowledge_base = json.load(file)

    def detect_requirements(self, requirement):
        text = requirement.lower()
        checks = [
            ("High Traffic", ["high traffic", "many users", "large number of users", "scalable", "scalability"]),
            ("Product Search", ["search", "product search", "find products"]),
            ("Product Catalog", ["product catalog", "product catalogue", "catalog", "catalogue", "products"]),
            ("Shopping Cart", ["cart", "shopping cart", "add to cart"]),
            ("Payment", ["payment", "online payment", "checkout", "transaction"]),
            ("Authentication", ["login", "authentication", "user authentication", "sign in"]),
            ("Security", ["security", "secure", "protection"]),
        ]
        detected = [label for label, keywords in checks if any(word in text for word in keywords)]
        return detected or ["General E-Commerce"]

    def get_technologies_for_requirements(self, detected_requirements):
        technologies = self.knowledge_base["technologies"]
        recommendations = []
        for requirement in detected_requirements:
            req = requirement.lower()
            for technology in technologies:
                purpose, name = technology["purpose"].lower(), technology["name"]
                match = (
                    (req == "product search" and ("search" in purpose or name == "OpenSearch")) or
                    (req == "product catalog" and ("product" in purpose or "catalog" in purpose or name in ["PostgreSQL", "OpenSearch"])) or
                    (req == "payment" and any(word in purpose for word in ["transactional", "authentication", "encrypted"])) or
                    (req == "authentication" and "authentication" in purpose) or
                    (req == "security" and technology["layer"].lower() == "security") or
                    (req == "high traffic" and name in ["Redis", "Kafka", "Kubernetes"]) or
                    (req == "shopping cart" and name in ["Redis", "PostgreSQL"]) or
                    (req == "general e-commerce" and technology["layer"] in ["Presentation", "Application", "Data", "API"])
                )
                if match:
                    recommendations.append(technology)
        unique = []
        for item in recommendations:
            if item not in unique:
                unique.append(item)
        return unique

    def get_components_for_requirements(self, detected_requirements):
        selected = []
        for component in self.knowledge_base["components"]:
            if any(req in component.get("requirements", []) for req in detected_requirements):
                selected.append(component)
        unique = []
        for item in selected:
            if item not in unique:
                unique.append(item)
        return unique

    def get_architecture_rules(self, detected_requirements):
        matched = []
        for rule in self.knowledge_base["selection_rules"]:
            condition = rule["condition"].lower()
            if any(req.lower() in condition for req in detected_requirements):
                matched.append(rule)
        return matched

    def get_architecture_patterns(self, detected_requirements):
        patterns = self.knowledge_base["architecture_patterns"]
        selected = []
        requirements_lower = [item.lower() for item in detected_requirements]
        for pattern in patterns:
            name = pattern["name"].lower()
            if "high traffic" in requirements_lower and ("microservices" in name or "event" in name):
                selected.append(pattern)
            if any(req in requirements_lower for req in ["product search", "product catalog", "shopping cart", "payment"]):
                if "three-tier" in name:
                    selected.append(pattern)
            if "payment" in requirements_lower and "event" in name:
                selected.append(pattern)
        unique = []
        for item in selected:
            if item not in unique:
                unique.append(item)
        return unique

    def generate_solution_1(self, detected_requirements, technologies, components, rules, patterns):
        solution = {"solution_name": "Solution 1", "architecture_style": [], "components": [], "technologies": [], "architecture_rules": []}
        solution["architecture_style"] = [pattern["name"] for pattern in patterns]
        solution["components"] = [{"name": c["name"], "purpose": c["purpose"]} for c in components]
        solution["technologies"] = [{"name": t["name"], "layer": t["layer"], "purpose": t["purpose"]} for t in technologies]
        solution["architecture_rules"] = [{"condition": r["condition"], "guidance": r["guidance"]} for r in rules]
        return solution

    def generate_hld(self, solution_1):
        hld = {"title": "E-Commerce High-Level Architecture", "architecture_style": solution_1["architecture_style"], "components": [], "technology_mapping": [], "connections": []}
        hld["components"] = [{"name": c["name"], "purpose": c["purpose"]} for c in solution_1["components"]]
        hld["technology_mapping"] = [{"technology": t["name"], "layer": t["layer"], "purpose": t["purpose"]} for t in solution_1["technologies"]]
        hld["connections"] = [
            {"from": "User", "to": "Product Service", "purpose": "Browse products"},
            {"from": "User", "to": "Search Service", "purpose": "Search products"},
            {"from": "User", "to": "Cart Service", "purpose": "Manage shopping cart"},
            {"from": "Cart Service", "to": "Order Service", "purpose": "Create order"},
            {"from": "Order Service", "to": "Payment Service", "purpose": "Process payment"},
            {"from": "Product Service", "to": "MongoDB", "purpose": "Store product catalog"},
            {"from": "Search Service", "to": "OpenSearch", "purpose": "Product search"},
            {"from": "Cart Service", "to": "Redis", "purpose": "Cart/session caching"},
            {"from": "Order Service", "to": "PostgreSQL", "purpose": "Store transactional data"},
            {"from": "Order Service", "to": "Kafka", "purpose": "Publish order events"},
            {"from": "Payment Service", "to": "PostgreSQL", "purpose": "Store payment/order state"},
        ]
        return hld

    def generate_mermaid_diagram(self, hld):
        mermaid = ["flowchart TD"]
        def node_id(name):
            result = re.sub(r"[^A-Za-z0-9_]", "_", name.replace(" ", "_"))
            if not result or result[0].isdigit():
                result = "node_" + result
            return result
        for connection in hld["connections"]:
            source, target = node_id(connection["from"]), node_id(connection["to"])
            label = connection["purpose"].replace('"', "'")
            source_label = connection["from"].replace('"', "'")
            target_label = connection["to"].replace('"', "'")
            mermaid.append(f'    {source}["{source_label}"] -->|"{label}"| {target}["{target_label}"]')
        return "\n".join(mermaid)

    def render_mermaid_diagram(self, mermaid_code, lld):
        lld_json = json.dumps(lld, ensure_ascii=False).replace("<", "\\u003c")
        safe_mermaid = html.escape(mermaid_code)
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ArchiGen AI - Interactive Architecture Blueprint</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 0; padding: 24px; background: #f3f6fa; color: #1f2937; }}
h1 {{ text-align: center; }} .intro {{ text-align: center; color: #64748b; line-height: 1.5; }}
.layout {{ display: grid; grid-template-columns: minmax(0, 2fr) minmax(290px, 1fr); gap: 20px; max-width: 1500px; margin: 24px auto; align-items: start; }}
.panel {{ background: white; padding: 22px; border-radius: 12px; box-shadow: 0 3px 14px rgba(0,0,0,.08); min-width: 0; }}
.diagram {{ overflow: auto; }} .mermaid {{ min-width: 600px; text-align: center; }}
.component-buttons {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 18px; }}
button {{ border: 1px solid #cbd5e1; background: #f8fafc; border-radius: 8px; padding: 9px 12px; cursor: pointer; font-size: 14px; }}
button:hover {{ background: #e8eef7; }} button:focus {{ outline: 2px solid #64748b; outline-offset: 2px; }}
.detail-section {{ margin-top: 16px; }} .detail-section h3 {{ margin-bottom: 6px; font-size: 15px; }} .detail-section ul {{ margin-top: 4px; padding-left: 20px; }}
.muted, .status {{ color: #64748b; }} .mermaid .node {{ cursor: pointer; }}
@media (max-width: 900px) {{ .layout {{ grid-template-columns: 1fr; }} body {{ padding: 14px; }} }}
</style>
<script>
window.archigenLld = {lld_json};
window.showLLD = function(componentName) {{
    const component = window.archigenLld.components.find(item => item.name === componentName);
    if (!component) return;
    const panel = document.getElementById("lld-details");
    panel.replaceChildren();
    const title = document.createElement("h2"); title.textContent = component.name; panel.appendChild(title);
    const purpose = document.createElement("p"); purpose.textContent = component.purpose || "Purpose not specified."; panel.appendChild(purpose);
    function addList(label, items) {{
        const section = document.createElement("section"); section.className = "detail-section";
        const h = document.createElement("h3"); h.textContent = label; section.appendChild(h);
        if (!items || !items.length) {{ const p = document.createElement("p"); p.className = "muted"; p.textContent = "No details provided yet."; section.appendChild(p); }}
        else {{ const ul = document.createElement("ul"); items.forEach(item => {{ const li = document.createElement("li"); li.textContent = item; ul.appendChild(li); }}); section.appendChild(ul); }}
        panel.appendChild(section);
    }}
    addList("Responsibilities", component.responsibilities);
    addList("APIs", component.apis);
    const store = document.createElement("p"); store.className = "detail-section"; store.textContent = "Data store: " + (component.data_store || "Not specified"); panel.appendChild(store);
    addList("Security", component.security);
    addList("Internal Operations", component.internal_operations);
}};
</script>
</head>
<body>
<h1>ArchiGen AI - Interactive Architecture Blueprint</h1>
<p class="intro">Select a service in the diagram or use a component button to view its Low-Level Design (LLD).</p>
<div class="layout">
<section class="panel diagram">
<h2>High-Level Design (HLD)</h2>
<div class="mermaid">
{safe_mermaid}
</div>
<h3>Choose a component</h3><div class="component-buttons" id="component-buttons"></div>
<p class="status" id="diagram-status">Loading architecture diagram…</p>
</section>
<aside class="panel" id="lld-details" aria-live="polite"><h2>Low-Level Design (LLD)</h2><p class="muted">Choose a component to view responsibilities, APIs, data store, security, and internal operations.</p></aside>
</div>
<script>
const buttons = document.getElementById("component-buttons");
window.archigenLld.components.forEach(component => {{
    const button = document.createElement("button"); button.type = "button"; button.textContent = component.name;
    button.addEventListener("click", () => window.showLLD(component.name)); buttons.appendChild(button);
}});
</script>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({{ startOnLoad: false, securityLevel: "strict", flowchart: {{ useMaxWidth: true, htmlLabels: true }} }});
try {{
    await mermaid.run({{ querySelector: ".mermaid" }});
    const svgNodes = document.querySelectorAll(".mermaid svg g.node");
    svgNodes.forEach(svgNode => {{
        const svgId = svgNode.id || "";
        const component = window.archigenLld.components.find(item => {{
            const expectedId = item.name.replace(/[^A-Za-z0-9_]/g, "_").replace(/\\s+/g, "_");
            return svgId.includes(expectedId);
        }});
        if (component) {{
            svgNode.style.cursor = "pointer"; svgNode.setAttribute("tabindex", "0"); svgNode.setAttribute("role", "button");
            svgNode.setAttribute("aria-label", "Show LLD for " + component.name);
            svgNode.addEventListener("click", () => window.showLLD(component.name));
            svgNode.addEventListener("keydown", event => {{ if (event.key === "Enter" || event.key === " ") {{ event.preventDefault(); window.showLLD(component.name); }} }});
        }}
    }});
    document.getElementById("diagram-status").textContent = "Diagram loaded. Click a service or use a component button to view its LLD.";
}} catch (error) {{
    console.error("Mermaid diagram failed to render:", error);
    document.getElementById("diagram-status").textContent = "Diagram could not load. Check your internet connection; component buttons should still work.";
}}
</script>
</body>
</html>'''
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(project_root, "architecture_diagram.html")
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        return output_path

    def generate_lld(self, hld):
        details = {
            "Product Service": {
                "responsibilities": ["Manage the product catalog", "Create, retrieve, update, and delete products", "Validate product information"],
                "apis": ["GET /products", "GET /products/{id}", "POST /products", "PUT /products/{id}", "DELETE /products/{id}"],
                "data_store": "MongoDB",
                "internal_operations": ["Validate product data", "Store product information", "Retrieve and update product information"],
            },
            "Search Service": {
                "responsibilities": ["Search products", "Filter and sort products", "Return relevant search results"],
                "apis": ["GET /search?q={query}", "GET /search/products"],
                "data_store": "OpenSearch",
                "internal_operations": ["Receive search query", "Validate search parameters", "Query OpenSearch and return results"],
            },
            "Cart Service": {
                "responsibilities": ["Create and retrieve a shopping cart", "Add or remove products", "Update item quantities"],
                "apis": ["GET /cart", "POST /cart/items", "PUT /cart/items/{id}", "DELETE /cart/items/{id}"],
                "data_store": "Redis (cart/session cache)",
                "internal_operations": ["Validate user/session", "Retrieve cart contents", "Update and cache cart information"],
            },
            "Order Service": {
                "responsibilities": ["Create orders", "Validate cart and order details", "Maintain order status"],
                "apis": ["POST /orders", "GET /orders/{id}", "GET /orders/{id}/status"],
                "data_store": "PostgreSQL",
                "internal_operations": ["Validate order request", "Create and persist order", "Publish order events to Kafka"],
            },
            "Payment Service": {
                "responsibilities": ["Validate payment requests", "Coordinate payment processing", "Track payment status"],
                "apis": ["POST /payments", "GET /payments/{id}", "GET /payments/{id}/status"],
                "data_store": "PostgreSQL (payment state; subject to final schema design)",
                "internal_operations": ["Validate payment request", "Call the configured payment provider", "Persist payment status and return the result"],
            },
        }
        lld = {"title": "E-Commerce Low-Level Design", "components": []}
        for component in hld.get("components", []):
            name = component["name"]
            item = details.get(name, {
                "responsibilities": [component.get("purpose", "Details not defined")],
                "apis": [], "data_store": "Not specified in the current prototype",
                "internal_operations": ["Details require further design"],
            })
            lld["components"].append({
                "name": name, "purpose": component.get("purpose", ""),
                "responsibilities": item["responsibilities"], "apis": item["apis"],
                "data_store": item["data_store"],
                "security": ["JWT-based API authentication where applicable", "TLS 1.3 for encrypted transport"],
                "internal_operations": item["internal_operations"],
            })
        return lld

    def analyze_requirement(self, requirement):
        detected_requirements = self.detect_requirements(requirement)
        technologies = self.get_technologies_for_requirements(detected_requirements)
        components = self.get_components_for_requirements(detected_requirements)
        rules = self.get_architecture_rules(detected_requirements)
        patterns = self.get_architecture_patterns(detected_requirements)
        solution_1 = self.generate_solution_1(detected_requirements, technologies, components, rules, patterns)
        hld = self.generate_hld(solution_1)
        lld = self.generate_lld(hld)
        mermaid_diagram = self.generate_mermaid_diagram(hld)
        diagram_path = self.render_mermaid_diagram(mermaid_diagram, lld)
        return {
            "domain": self.knowledge_base["domain"], "original_requirement": requirement,
            "detected_requirements": detected_requirements, "recommended_technologies": technologies,
            "components": components, "architecture_rules": rules, "architecture_patterns": patterns,
            "solution_1": solution_1, "hld": hld, "lld": lld,
            "mermaid_diagram": mermaid_diagram, "diagram_path": diagram_path,
        }


if __name__ == "__main__":
    agent = ArchiGenAgent()
    requirement = """
    Build an e-commerce application with high traffic,
    products, product search, shopping cart and online payment.
    """
    result = agent.analyze_requirement(requirement)
    print("\n===== ARCHIGEN AI =====")
    print("\nDomain:\n" + str(result["domain"]))
    print("\nOriginal Requirement:\n" + result["original_requirement"])
    print("\nDetected Requirements:")
    for requirement in result["detected_requirements"]:
        print(f"✓ {requirement}")
    print("\nRecommended Technologies:")
    for technology in result["recommended_technologies"]:
        print(f"- {technology['name']} [{technology['layer']}] → {technology['purpose']}")
    print("\nArchitecture Components:")
    for component in result["components"]:
        print(f"- {component['name']} → {component['purpose']}")
    print("\nArchitecture Rules:")
    for rule in result["architecture_rules"]:
        print(f"- {rule['condition']} → {rule['guidance']}")
    print("\nArchitecture Patterns:")
    for pattern in result["architecture_patterns"]:
        print(f"- {pattern['name']} → {pattern['description']}")
    print("\n===== SOLUTION 1 =====")
    print("\nArchitecture Style:")
    for style in result["solution_1"]["architecture_style"]:
        print(f"- {style}")
    print("\nComponents:")
    for component in result["solution_1"]["components"]:
        print(f"- {component['name']} → {component['purpose']}")
    print("\nTechnologies:")
    for technology in result["solution_1"]["technologies"]:
        print(f"- {technology['name']} [{technology['layer']}] → {technology['purpose']}")
    print("\nArchitecture Rules:")
    for rule in result["solution_1"]["architecture_rules"]:
        print(f"- {rule['condition']} → {rule['guidance']}")
    print("\n===== HIGH-LEVEL DESIGN =====")
    print("\nTitle:\n" + result["hld"]["title"])
    print("\nArchitecture Style:")
    for style in result["hld"]["architecture_style"]:
        print(f"- {style}")
    print("\nHLD Components:")
    for component in result["hld"]["components"]:
        print(f"- {component['name']} → {component['purpose']}")
    print("\nTechnology Mapping:")
    for technology in result["hld"]["technology_mapping"]:
        print(f"- {technology['technology']} [{technology['layer']}] → {technology['purpose']}")
    print("\nHigh-Level Connections:")
    for connection in result["hld"]["connections"]:
        print(f"- {connection['from']} → {connection['to']} → {connection['purpose']}")
    print("\n===== LOW-LEVEL DESIGN =====")
    print(result["lld"]["title"])
    for component in result["lld"]["components"]:
        print("\n----------------------------------------")
        print(f"\nComponent: {component['name']}\nPurpose: {component['purpose']}")
        print("\nResponsibilities:")
        for item in component["responsibilities"]: print(f"- {item}")
        print("\nAPIs:")
        for api in component["apis"]: print(f"- {api}")
        print(f"\nData Store: {component['data_store']}")
        print("\nSecurity:")
        for item in component["security"]: print(f"- {item}")
        print("\nInternal Operations:")
        for item in component["internal_operations"]: print(f"- {item}")
    print("\n===== MERMAID ARCHITECTURE DIAGRAM =====")
    print("\n```mermaid")
    print(result["mermaid_diagram"])
    print("```")
    print("\n===== VISUAL ARCHITECTURE DIAGRAM =====")
    print("Architecture diagram generated successfully.")
    print(f"Open this file in your browser:\n{result['diagram_path']}")
