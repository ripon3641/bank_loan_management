# -*- coding:utf-8 -*-

{
    'name': 'Bank Loan Management',
    'version': '15.0.0',
    'category': 'Accounting',
    'author': 'Ripon Hossain',
    'sequence': -1000,
    'summary': 'Bank Loan Management',
    'description':"""
        <p>Manage and track bank loans with ease using the Bank Loan Management app.</p>
        
        <h2>Key Features:</h2>
        <ul>
            <li>Efficiently manage loan applications and approvals.</li>
            <li>Track loan disbursements and repayments.</li>
            <li>Generate loan statements and reports.</li>
            <li>Automate interest calculations and payment reminders.</li>
        </ul>
        
        <h2>Benefits:</h2>
        <ul>
            <li>Streamline the loan application process for customers.</li>
            <li>Ensure accurate loan tracking and compliance.</li>
            <li>Reduce administrative overhead and paperwork.</li>
            <li>Gain insights with comprehensive loan analytics.</li>
        </ul>
        
        <p>Experience the convenience of managing bank loans with our powerful Bank Loan Management app.</p>
        
        <p><strong>Get started today!</strong></p>
    """,
    'depends': ['mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/bank_loan_management.xml',
        'views/loan_configurations.xml',
        'views/loan_type_config.xml',
        'views/loan_installment.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'licence': 'LGPL-3',
    'icon': 'static/icon.png',
    'images': ['static/description/icon.png'],
}