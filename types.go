type WappDomSelector struct {
	RawContent []string          `json:"__raw_content"`
	Attributes map[string]string `json:"attributes"`
}

type WappTechnologyData struct {
	Name        string              `json:"name"`
	Cats        []int               `json:"cats"`
	Website     string              `json:"website"`
	Description string              `json:"description"`
	Icon        string              `json:"icon"`
	CPE         string              `json:"cpe"`
	Saas        bool                `json:"saas"`
	OSS         bool                `json:"oss"`
	Pricing     []string            `json:"pricing"`
	Implies     []string            `json:"implies"`
	Requires    []string            `json:"requires"`
	Excludes    []string            `json:"excludes"`
	DOM         WappDomSelector     `json:"dom"`
	Cookies     map[string]string   `json:"cookies"`
	DNS         map[string][]string `json:"dns"`
	JS          map[string]string   `json:"js"`
	Headers     map[string]string   `json:"headers"`
	HTML        []string            `json:"html"`
	CSS         []string            `json:"css"`
	Robots      []string            `json:"robots"`
	URL         string              `json:"url"`
	XHR         []string            `json:"xhr"`
	Meta        map[string][]string `json:"meta"`
	ScriptSrc   []string            `json:"scriptSrc"`
	Scripts     []string            `json:"scripts"`
}