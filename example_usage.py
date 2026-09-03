from client import PullRequestSemanticRiskBlastRadiusScorerClient

def main():
    client = PullRequestSemanticRiskBlastRadiusScorerClient()
    res = client.score_pull_request_risk('diff ...', 2, False)
    print('PR Semantic Risk Scorer: ' + res['risk_assessment_id'] + ' (' + res['risk_level'] + ')')
    print('Risk Score: ' + str(res['overall_risk_score']) + ' | Mitigations: ' + res['suggested_mitigations'][0])
    print('Report URL: ' + res['pr_risk_report_markdown_url'])

if __name__ == '__main__':
    main()
